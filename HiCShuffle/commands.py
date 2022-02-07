import argparse
import textwrap
import sys

def panchip_parser():
    usage = '''\
        panchip <command> [options]
        Commands:
            diff            FASTQ Shuffling Tool For Sanity Check in Hi-C Differential Contact Analysis
        Run panchip <command> -h for help on a specific command.
        '''
    parser = argparse.ArgumentParser(
        description='HiCShuffle: FASTQ Shuffling Tool For Sanity Check in Hi-C Differential Contact Analysis',
        usage=textwrap.dedent(usage)
    )

    from .version import __version__
    parser.add_argument('--version', action='version', version=f'HiCShuffle {__version__}')
    
    parser.add_argument('command', nargs='?', help='Subcommand to run')

    return parser

def diff_parser():
    parser = MyParser(
        description='FASTQ Shuffling Tool For Sanity Check in Hi-C Differential Contact Analysis',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        prog='panchip diff'
    )

    parser.add_argument(
        'library_directory',
        type=str,
        help='Directory wherein PanChIP library will be stored. > 4.2 GB of storage required.')
    
    parser.add_argument(
        'output_directory',
        type=str,
        help='Output directory wherein output files will be stored.')
    
    parser.add_argument(
        '-t',
        dest='threads',
        type=int,
        default=1,
        help='Number of threads to use.')
    
    parser.add_argument(
        '-r',
        dest='repeats',
        type=int,
        default=1,
        help='Number of repeats to perform.')

    return parser
      
class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)
