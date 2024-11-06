from typing import Optional

import typer
from rich import print as pprint

from exporters.export import Export
from exporters.to_json import JsonExport
from parsers.otodom import OtoDomParser
from parsers.otomoto import OtoMotoParser
from parsers.parser import Parser
from scrapers.otodom import OtoDomScraper
from scrapers.otomoto import OtoMotoScraper
from scrapers.scraper import PageScraper

app = typer.Typer()


@app.command()
def main(
        url: str,
        page_limit: Optional[int] = None,
        export_to: Optional[str] = "json",
) -> None:
    parsed_data = None

    otomoto_scraper = OtoMotoScraper()
    otodom_scraper = OtoDomScraper()

    otomoto_parser = OtoMotoParser()
    otodom_parser = OtoDomParser()

    if "otomoto" in url:
        page_scraper_otomoto = PageScraper(scraper_strategy=otomoto_scraper)
        scraped_data = page_scraper_otomoto.scrape(url=url, page_limit=page_limit)
        otomoto_page_parser = Parser(parser_strategy=otomoto_parser)
        parsed_data = otomoto_page_parser.parse(data=scraped_data)

    elif "otodom" in url:
        page_scraper_otodom = PageScraper(scraper_strategy=otodom_scraper)
        scraped_data = page_scraper_otodom.scrape(url=url, page_limit=page_limit)
        otodom_page_parser = Parser(parser_strategy=otodom_parser)
        parsed_data = otodom_page_parser.parse(data=scraped_data)

    else:
        print("Invalid url")

    if export_to == "json":
        if not parsed_data:
            print("No data")

        pprint(parsed_data)

        json_export = JsonExport()
        export = Export(strategy=json_export)
        export.export(parsed_data=parsed_data)

    else:
        print("Invalid export format")


if __name__ == "__main__":
    app()
