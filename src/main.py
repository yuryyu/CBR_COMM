import argparse
from .graph import Graph
from .features.feature_list import featurizer_list, featurize


def main():
    parseargs = argparse.ArgumentParser()
    parseargs.add_argument("filename", type=str, help="add an input graph csv file in edge list format")
    parseargs.add_argument("-o", "--output", type=str, default="output.csv", help="add an output file name")
    args = parseargs.parse_args()

    graph = Graph.load_from_csv(args.filename)
    features = featurize(featurizer_list, graph)
    names = [feat.name for feat in features]
    vals = [feat.value for feat in features]
    with open(args.output, 'w') as f:
        f.write(",".join(names)+"\n")
        f.write(",".join(["%.3f" % val for val in vals]) + "\n")


if __name__ == '__main__':
    main()
