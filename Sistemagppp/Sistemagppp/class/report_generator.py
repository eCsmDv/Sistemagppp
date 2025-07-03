from abc import ABC, abstractmethod

class Report(ABC):
    @abstractmethod
    def generate(self) -> str:
        pass

class PDFReport(Report):
    def generate(self) -> str:
        return "Relatório gerado em PDF."

class ReportDecorator(Report):
    def __init__(self, report: Report):
        self._report = report

    @abstractmethod
    def generate(self) -> str:
        pass

class HeaderDecorator(ReportDecorator):
    def generate(self) -> str:
        return "Cabeçalho\n" + self._report.generate()

class TimestampDecorator(ReportDecorator):
    def generate(self) -> str:
        from datetime import datetime
        return self._report.generate() + f"\nGerado em: {datetime.now()}"
