from csv import Sniffer, DictReader, DictWriter

class CSVUtil:

    @staticmethod
    def read(file):

        with open(file, "r") as csv:

            sniffer = Sniffer()
            sample = csv.read(4096)
            dialect = sniffer.sniff(sample, delimiters=[';', ','])

            csv.seek(0)

            lines_reader = DictReader(csv, dialect=dialect)

            lines = []
            for line in lines_reader:
                lines.append(line)

            return lines, lines_reader.fieldnames

    @staticmethod
    def write(file, lines, delimiter=';'):

        with open(file, 'w') as csv:

            if len(lines) == 0:
                return

            fieldnames = list(lines[0].keys())
            writer = DictWriter(csv, delimiter=delimiter, fieldnames=fieldnames)
            writer.writerow(dict((fn,fn) for fn in fieldnames))

            for line in lines:
                writer.writerow(line)