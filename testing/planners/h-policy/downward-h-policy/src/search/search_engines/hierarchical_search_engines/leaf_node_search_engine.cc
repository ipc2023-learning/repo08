#include "leaf_node_search_engine.h"

#include "goal_test.h"

#include "../../option_parser.h"
#include "../../plugin.h"
#include "../../tasks/root_task.h"
#include "../../tasks/propositional_task.h"
#include "../../task_utils/successor_generator.h"
#include "../../task_utils/task_properties.h"
#include "../../utils/logging.h"
#include "../../utils/memory.h"
#include "../../utils/timer.h"


#include <cassert>
#include <cstdlib>

using namespace std;


namespace hierarchical_search_engine {


SearchStatus LeafNodeSearchEngine::step() {
    // cout << "LeafNodeSearchEngine::step" << endl;
    State initial_state = m_state_registry->lookup_state(m_initial_state_id);
    /* Goal check in initial state of subproblem. */
    if (is_goal(initial_state)) {
        m_partial_solutions = {PartialSearchSolution{{}, initial_state.get_id()}};
        return SearchStatus::CYCLE;
    }

    /* Generate successors */
    vector<OperatorID> applicable_ops;
    successor_generator.generate_applicable_ops(initial_state, applicable_ops);
    for (auto op_id : applicable_ops) {
        OperatorProxy op = task_proxy.get_operators()[op_id];
        State succ_state = m_state_registry->get_successor_state(initial_state, op);
        statistics.inc_generated();
        if (m_debug)
            std::cout << get_name() << " succ_state: " << m_propositional_task->compute_dlplan_state(succ_state).str() << std::endl;
        if (is_goal(succ_state)) {
            if (m_debug)
                std::cout << op.get_name() << " " << get_name() << " goal_state: " << m_propositional_task->compute_dlplan_state(succ_state).str() << std::endl;
            // set the solution.
            m_partial_solutions = {PartialSearchSolution{Plan{OperatorID(op.get_id())}, succ_state.get_id()}};
            return SearchStatus::SOLVED;
        }
    }
    return SearchStatus::FAILED;
}


LeafNodeSearchEngine::LeafNodeSearchEngine(const options::Options &opts)
   : HierarchicalSearchEngine(opts) {
    m_name = "LeafNodeSearchEngine";
   }

void LeafNodeSearchEngine::print_statistics() const {

}

static shared_ptr<SearchEngine> _parse(OptionParser &parser) {
    parser.document_synopsis("Leaf node search engine.", "");
    HierarchicalSearchEngine::add_goal_test_option(parser);
    SearchEngine::add_options_to_parser(parser);

    Options opts = parser.parse();
    if (parser.dry_run()) {
        return nullptr;
    }
    return make_shared<LeafNodeSearchEngine>(opts);
}

static Plugin<SearchEngine> _plugin("leaf_node_search", _parse);
}
