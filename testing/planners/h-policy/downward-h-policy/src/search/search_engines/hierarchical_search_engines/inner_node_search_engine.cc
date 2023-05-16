#include "inner_node_search_engine.h"

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

static std::vector<std::shared_ptr<HierarchicalSearchEngine>>
to_hierarchical_search_engines(const std::vector<std::shared_ptr<SearchEngine>>& child_search_engines) {
    std::vector<std::shared_ptr<HierarchicalSearchEngine>> result;
    for (std::shared_ptr<SearchEngine> child_search_engine : child_search_engines) {
        result.push_back(std::dynamic_pointer_cast<HierarchicalSearchEngine>(child_search_engine));
    }
    return result;
}


SearchStatus InnerNodeSearchEngine::step() {
    // cout << "InnerNodeSearchEngine::step" << endl;
    State current_state = m_state_registry->lookup_state(m_initial_state_id);
    std::unordered_set<int> visited;
    visited.insert(current_state.get_id().value);
    while (!is_goal(current_state)) {
        bool stepped = false;
        for (auto& child_search_engine : m_child_search_engines) {
            child_search_engine->set_initial_state(current_state);
            if (child_search_engine->get_goal_test().is_applicable()) {
                SearchStatus child_search_status = child_search_engine->step();
                if (child_search_status == SOLVED) {
                    PartialSearchSolutions child_partial_solutions = child_search_engine->get_partial_solutions();
                    m_partial_solutions.insert(m_partial_solutions.end(), child_partial_solutions.begin(), child_partial_solutions.end());
                    current_state = m_state_registry->lookup_state(child_partial_solutions.back().state_id);
                    if (!visited.insert(current_state.get_id().value).second) {
                        return SearchStatus::CYCLE;
                    }
                    stepped = true;
                    break;
                }
                return child_search_status;
            }
        }
        if (!stepped) {
            return SearchStatus::FAILED;
        }
    }
    return SearchStatus::SOLVED;
}


InnerNodeSearchEngine::InnerNodeSearchEngine(const options::Options &opts)
   : HierarchicalSearchEngine(opts) {
   m_child_search_engines = to_hierarchical_search_engines(opts.get_list<std::shared_ptr<SearchEngine>>("child_searches"));
   m_name = "InnerNodeSearchEngine";
}

void InnerNodeSearchEngine::print_statistics() const {

}

static shared_ptr<SearchEngine> _parse(OptionParser &parser) {
    parser.document_synopsis("Leaf node search engine.", "");
    HierarchicalSearchEngine::add_goal_test_option(parser);
    HierarchicalSearchEngine::add_child_search_engine_option(parser);
    SearchEngine::add_options_to_parser(parser);

    Options opts = parser.parse();
    if (parser.dry_run()) {
        return nullptr;
    }
    return make_shared<InnerNodeSearchEngine>(opts);
}

static Plugin<SearchEngine> _plugin("inner_node_search", _parse);
}
