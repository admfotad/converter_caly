import argparse

FORMATS = {
    # 'csv': CsvFormat
}


def main():
    parser = argparse.ArgumentParser(description='Convert types of data')
    parser.add_argument('infile')
    parser.add_argument('outfile')
    parser.add_argument('-i', '--input-format')
    parser.add_argument('-o', '--output-format')
    parser.add_argument(
        '-p', '--pretty-print', action='store_true',
        help='Pretty print if available'
    )

    args = parser.parse_args()

    InputFormat = FORMATS[args.input_format]
    OutputFormat = FORMATS[args.output_format]
    with open(args.infile) as f:
        input_format = InputFormat(f)
        data = input_format.read()
    with open(args.outfile):
        output_format = OutputFormat(f, pretty=args.pretty_print)
        output_format.write(data)


if __name__ == '__main__':
    main()
