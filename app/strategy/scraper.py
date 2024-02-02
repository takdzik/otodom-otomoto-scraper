from abc import ABC, abstractmethod
from .params import ParamsBase
from typing import Optional


class ScrapeStrategy(ABC):

    @abstractmethod
    def scrape(self, params: ParamsBase, url: Optional[str] = None):
        pass


class Scraper:
    def __init__(self, scraper_strategy: ScrapeStrategy):
        self.scraper_strategy = scraper_strategy

    def scrape(self, params: Optional[ParamsBase] = None, url: Optional[str] = None):
        self.scraper_strategy.scrape(params, url)
