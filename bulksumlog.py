import argparse
import logging
import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions


class scrip_val(beam.DoFn):
    def process(self, element):
        try:
            line = element[0:element.find('"', 1)] + element[element.find('"', 1) + 1: \
            element.find('"', element.find('"', 1) + 1)].replace(',','') + element[element.find('"', element.find('"',1) + 1) + 1:]
            if line.split(',')[4] == 'BUY':
                tp=line.split(',')[1]+','+line.split(',')[5]
            else:
                tp=line.split(',')[1]+',-'+line.split(',')[5]
            tp=tp.split()
            return tp
        except:
            logging.info('Some Error occured')
def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input',
                        dest='input',
                        default='gs://pydataflow',
                        help='Input file to process.')
    parser.add_argument('--output',
                        dest='output',
                        required=True,
                        help='Output file to write results to.')
    known_args, pipeline_args = parser.parse_known_args()
    def count_ones(word_ones):
        (word, ones) = word_ones
        return (word, sum(ones))
    def format_result(bulk_deal):
        (bulk, deal) = bulk_deal
        return '%s: %d' % (bulk, deal)
    with beam.Pipeline(options=PipelineOptions(pipeline_args)) as p:
        lines = p | 'read' >> ReadFromText(known_args.input)
        counts = (
                lines
                | 'Get required tuple' >> beam.ParDo(scrip_val())
                | 'PairWithValue' >> beam.Map(lambda x: (x.split(',')[0],int(x.split(',')[1])))
                | 'group' >> beam.GroupByKey()
                | 'Summing' >> beam.Map(count_ones)
        )
        output = counts | 'format' >> beam.Map(format_result)
        output | 'write' >> WriteToText(known_args.output)
if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    run()