import downloader
import logger
import generator


if __name__ == "__main__":
    logger.initialization()
    downloader.download()
    generator.generate()