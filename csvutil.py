from csv import Sniffer, DictReader, DictWriter

class CSVUtil:

    @staticmethod
    def read(filename):

        with open(filename, "r") as csv:

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
    def write(filename, lines, delimiter=';'):

        with open(filename, 'w') as csv:

            if len(lines) == 0:
                return

            fieldnames = list(lines[0].keys())
            writer = DictWriter(csv, delimiter=delimiter, fieldnames=fieldnames)
            writer.writerow(dict((fn,fn) for fn in fieldnames))

            for line in lines:
                writer.writerow(line)