#ifndef SEARCH_ENGINES_INNER_NODE_SEARCH_ENGINE_H
#define SEARCH_ENGINES_INNER_NODE_SEARCH_ENGINE_H

#include "hierarchical_search_engine.h"

namespace options {
class Options;
}

namespace hierarchical_search_engine {
class InnerNodeSearchEngine : public HierarchicalSearchEngine {
private:
    HierarchicalSearchEngine* m_active_search_engine;

protected:
    virtual SearchStatus step() override;

public:
    explicit InnerNodeSearchEngine(const options::Options &opts);

    virtual void print_statistics() const override;
};
}

#endif
