import graphlab
import argparse
import sys

# --------------------------------------------------
def get_args():
    """get args"""
    parser = argparse.ArgumentParser(
        description='Independant model evaluation',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-f', '--file', help='imput kmer frequency table',
                        metavar='file', type=str)
    parser.add_argument('-o', '--out', help='output file',
                        metavar='out', type=str)
    parser.add_argument('-m', '--mod', help='model path',
                        metavar='mod', type=str)

    return parser.parse_args()

def main():
    args = get_args()
    my_file = args.file
    my_out = args.out
    my_model = args.mod
    
    # # import data in SFRAME
    model = graphlab.load_model(model_name)
    print("################model "+model_name+"loaded ##############")
    
    evalData=graphlab.SFrame()
    evalData=graphlab.SFrame.read_csv(my_file, delimiter="\t", header=True)
    
    print("###############Begin models evaluation#############")
    classification = model.classify(evalData)
    classification.add_column(evalData["seq_id"],"seq_id")
    
    classification.export_csv(my_out, delimiter='\t', line_terminator='\n', header=True)

if __name__ == '__main__':
    main()
