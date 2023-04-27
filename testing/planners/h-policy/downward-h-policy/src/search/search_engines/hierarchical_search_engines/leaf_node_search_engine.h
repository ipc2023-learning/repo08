#ifndef SEARCH_ENGINES_LEAF_NODE_SEARCH_ENGINE_H
#define SEARCH_ENGINES_LEAF_NODE_SEARCH_ENGINE_H

#include "hierarchical_search_engine.h"

namespace options {
class Options;
}

namespace hierarchical_search_engine {
class LeafNodeSearchEngine : public HierarchicalSearchEngine {
protected:
    virtual SearchStatus step() override;

public:
    explicit LeafNodeSearchEngine(const options::Options &opts);

    virtual void print_statistics() const override;
};
}

#endif
