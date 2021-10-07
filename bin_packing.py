import argparse
import predict_heuristic
from Base import bp2DSimpleHeuristics
from Base.bp2DSimpleHeuristics import single_type_heuristic, first_fit_decreasing, get_all_heuristics
from Base.bpReadWrite import ReadWrite


def main():
    print("In bin_packing.py")
    iFile = args.file

    heuristic_name = predict_heuristic.predict(iFile)
    for label, (name, method) in enumerate(get_all_heuristics()):
        if name == heuristic_name:
            heuristic_meth = method

    state = ReadWrite.read_state(iFile)
    single_type_heuristic(state, heuristic_step=heuristic_meth)
    ReadWrite.write_state(path=iFile+"_solution", state=state)

    ##CHecking
    state = ReadWrite.read_state(iFile)
    solution = ReadWrite.read_state(path=iFile+"_solution")
    print(f"Is solution valid? {solution.is_valid(state)}!")


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Predict suitable heuristic for input state')
    parser.add_argument('-f', '--file', required=True, type=str, help='Input file location in the format '
                                                                      'path/to/file/filename.extension')
    args = parser.parse_args()
    main()
