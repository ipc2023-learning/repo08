#ifndef SEARCH_ENGINES_HIERARCHICAL_SEARCH_ENGINE_H
#define SEARCH_ENGINES_HIERARCHICAL_SEARCH_ENGINE_H

#include "goal_test.h"

#include "../../search_engine.h"
#include "../../state_id.h"

#include <memory>
#include <vector>


namespace options {
class Options;
class OptionParser;
}

namespace hierarchical_search_engine {
class InnerNodeSearchEngine;
class LeafNodeSearchEngine;


struct PartialSearchSolution {
    // The applied actions
    Plan plan;
    // The reached state
    StateID state_id;

    PartialSearchSolution() :
        state_id(StateID::no_state) { }

    PartialSearchSolution(Plan plan, StateID state_id)
        : plan(plan), state_id(state_id) { }
};

using PartialSearchSolutions = std::vector<PartialSearchSolution>;


class HierarchicalSearchEngine : public SearchEngine {

friend class IWSearch;
friend class InnerNodeSearchEngine;

protected:
    std::string m_name;

    std::shared_ptr<StateRegistry> m_state_registry;
    std::shared_ptr<extra_tasks::PropositionalTask> m_propositional_task;
    std::shared_ptr<goal_test::GoalTest> m_goal_test;

    std::vector<std::shared_ptr<HierarchicalSearchEngine>> m_child_search_engines;

    // maximum bound until search terminates
    int m_bound;

    StateID m_initial_state_id;

    PartialSearchSolutions m_partial_solutions;

    bool m_debug;

protected:
    /**
     * Performs task transformation to ModifiedInitialStateTask.
     */
    explicit HierarchicalSearchEngine(const options::Options &opts);

    /**
     * Top-level initialization.
     */
    virtual void initialize() override;

    virtual bool is_goal(const State &state);

    /**
     * Child-level initialization.
     */
    virtual void set_state_registry(std::shared_ptr<StateRegistry> state_registry);
    virtual void set_propositional_task(std::shared_ptr<extra_tasks::PropositionalTask> propositional_task);

    /**
     * Setters.
     * Returns true iff search engine provides additional subgoal states.
     */
    virtual void set_initial_state(const State& state);

    /**
     * Getters.
     */
    virtual std::string get_name();
    virtual SearchStatistics collect_statistics() const;
    const goal_test::GoalTest& get_goal_test() const;
    PartialSearchSolutions get_partial_solutions() const;

public:
    static void add_child_search_engine_option(options::OptionParser &parser);
    static void add_goal_test_option(options::OptionParser &parser);

    virtual void search() override;
};
}

#endif
