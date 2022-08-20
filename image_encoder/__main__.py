import sys

from image_encoder.ports.cli import Cli

def main():
    args = Cli.parse_args(*sys.argv[1:])

    cli_object = Cli()

    return cli_object.run(args)


# python -m image_encoder --mode encoding --message 'test message' --img-name test_image.png
# python -m image_encoder --mode decoding --img-name test_image_encoded.png 
#
if __name__ == "__main__":

    print("#############\nIMAGE_ENCODER\n#############\n")
    run = main
    sys.exit(run())