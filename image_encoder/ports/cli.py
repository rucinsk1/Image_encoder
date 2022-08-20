import argparse
from image_encoder.domain.logger import get_logger
from image_encoder.domain.decode import decode
from image_encoder.domain.encode import encode


logger = get_logger()

class Cli:

        
    modes = {
        "encoding",
        "decoding",
    }

    def run(self, namespace: argparse.Namespace):
        
        def print_info(mode, message, img_name):
            logger.debug(f"Running in {mode} mode")
            if mode == "encoding":
                logger.debug(f"encoding message: {message}")
                logger.debug(f"Using image: {img_name}")
            else:
                logger.debug(f"Decoding from image: {img_name}")
            

        mode = namespace.mode
        message = namespace.message
        img_name = namespace.img_name
        
        print_info(mode, message, img_name)

        if mode == 'encoding':
            encode(message, img_name)
        else:
            decoded_message = decode(img_name)
            logger.debug(f"Decoded message: {decoded_message}")


        



        #logger.debug(f"saved prediction result to {saved}")


    @staticmethod
    def parse_args(*args: str) -> argparse.Namespace:
        parser = argparse.ArgumentParser(
            description="This app runs encoding/decoding"
        )

        parser.add_argument(
            "--mode",
            choices=Cli.modes,
            help="mode in which app should run",
            required=True,
        )

        parser.add_argument(
            "--message",
            type=str,
            help="message to decode",
            required=False,
        )

        parser.add_argument(
            "--img-name",
            type=str,
            help="name of the image (with extension)",
            required=True,
        )

        namespace = parser.parse_args(args)

        # validate args
        mode = namespace.mode
        if mode not in Cli.modes:
            raise ValueError(f"Unknown mode: {namespace.mode}")

        img_name = namespace.img_name
        if img_name is None:
            raise ValueError("--img-name should be a valid name")
        
        message = namespace.message
        if message is None and mode == "encoding":
            raise ValueError("--message should be a valid string (in encoding mode)")
        
        #TODO raise exceptions if file odesnt match format


        return namespace
