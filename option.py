import sys
from logging import error
from optparse import OptionParser

def prepare_parameters():
    version = "Dot stripper v0.0"
    description = "This program stript dot from all kind of refSeq ID that contain a dot in transcript ID."
    usage = """
    stripDOT [OPTION] [Parameters]
    --input     -i [file path] input file directory
    --targetCol -c [integer number] which coloumn contain transcript ID, default = 3 (bed format)
    --symbol    -s [text] what kind of symbol need to be strip, default = "."
    --outFile -o [file path/output file.txt] output file directory
    """
    
    opt = OptionParser(
        version = version,
        description = description,
        usage = usage,
        add_help_option = False
        )

    opt.add_option("-h","--help",action="help",help="Show help message.")
    opt.add_option("-i","--input",
                   dest="in_file",
                   type="string",
                   help="Please select a bed format file.")
    opt.add_option("-c","--targetCol",
                   dest="num",
                   type="int",
                   help="Please enter column number.")
    opt.add_option("-s","--symbol",
                   dest="symbol",
                   type="string",
                   help="Please enter target symbol.")
    opt.add_option("-o","--output_file",
                   dest="out_file",
                   type="string",
                   help="Please select output file directory.")  

    return opt

def parameter_validate(optparser):
    (options,args) = optparser.parse_args()
    
    # Check input file
    if not options.in_file:
        optparser.print_help()
        error("No input file!")
        sys.exit(1)
    elif options.in_file[-4:] != ".bed":
        optparser.print_help()
        error("Please select a bed file!")
        sys.exit(1)
    
    # Check target column
    if not options.num:
        options.num = 3
    elif not str.isnumeric(options.num):
        optparser.print_help()
        error("Please enter column number (integer)")
        sys.exit(1)
    
    # Check target symbol
    # Default was set to "."
    if not options.symbol:
        options.symbol = "."
        
    # Check output file
    # Default was set to "./converted.txt"
    if not options.out_file:
        options.out_file = "./converted.txt"
        
    return options

if __name__=="__main__":
    print("""
    stripDOT [OPTION] [Parameters]
    --input     -i [file path] input file directory
    --targetCol -c [integer number] which coloumn contain transcript ID, default = 3 (bed format)
    --symbol    -s [text] what kind of symbol need to be strip, default = "."
    --outDirPrefix -o [file path] output file directory
    """)