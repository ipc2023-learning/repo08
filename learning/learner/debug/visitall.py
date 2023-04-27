from sketch_learning.util.misc import update_dict


def experiments():
    base = dict(
        domain_dir="visitall",
    )

    exps = dict()

    strips_base = update_dict(
        base,
        domain="domain",
    )

    exps["sketch_debug"] = update_dict(
        strips_base,
        pipeline="sketch_pipeline",
        instances=training_instances(),
        debug_features=["n_count(c_not(c_primitive(visited,0)))",  # 3
                        "n_concept_distance(c_primitive(at-robot,0),r_primitive(connected,0,1),c_not(c_primitive(visited,0)))",  # 5
                        "n_concept_distance(c_primitive(at-robot,0),r_primitive(connected,0,1),c_not(c_all(r_restrict(r_primitive(connected,0,1),c_primitive(visited_g,0)),c_primitive(visited,0))))",
                        #"n_count(c_and(c_primitive(visited_g,0),c_some(r_inverse(r_primitive(connected,0,1)),c_primitive(at-robot,0))), )"
        ],
    )

    exps["sketch"] = update_dict(
        strips_base,
        pipeline="sketch_pipeline",
        instances=training_instances(),
        max_states_per_instance=5000,
    )

    exps["hierarchy"] = update_dict(
        strips_base,
        pipeline="hierarchy_pipeline",
        instances=training_instances(),
        max_states_per_instance=5000,
    )

    return exps

def instances():
    return ["p-2-1.0-3-0"]

def training_instances():
    return [f"p-{unavail}-{pct}-{grid_size}-{seed}" for unavail in range(1,3) for pct in [0.5,1.0] for grid_size in range(2,5) for seed in range(0,10) ]
