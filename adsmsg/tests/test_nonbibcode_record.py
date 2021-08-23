
import unittest
from adsmsg import msg
from google.protobuf import json_format

from adsmsg.nonbibrecord import NonBibRecord, DataLinksRecord, DataLinksRecordList, \
    DocumentRecord, DocumentRecords, DataSource, DataSourceList

class TestMsg(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)


    def test_nonbib(self):
        """test creation of protobuf 

        should include at least all fields listed AdsDataSqlSync:adsdata/run.py:nonbib_to_master_fields"""
        nonbib_data = {'bibcode': '2003ASPC..295..361M', 
                       'boost': 3.1,
                       'citation_count': 3,
                       'bibgroup': ["Chandra/Technical"],
                       'bibgroup_facet':  ["Chandra/Technical"],
                       'data': ['NED:15', 'CDS:5'],
                       'data_links_rows': [{'link_type': 'a', 'link_sub_type': 'b', 
                                            'url': ['http://a', 'http://b'],
                                            'title': ['x', 'y'],
                                            'item_count':1},
                                           {'link_type': 'aa', 'link_sub_type': 'bb', 
                                            'url': ['http://aa', 'http://bb'],
                                            'title': ['xx', 'yy'],
                                            'item_count':2}],
                       'citation_count_norm': .2,
                       'esource': ['a', 's', 'd', 'f'],
                       'grants': ['g1', 'g2'],
                       'ned_objects': ['ned1', 'ned2'],
                       'norm_cites': 2,
                       'read_count': 7,
                       'readers': ['r1', 'r2'],
                       'reference': ['ref1', 'ref2'],
                       'simbad_objects': ['s1', 's2'],
                       'total_link_counts': 20
                       }
        m = NonBibRecord(**nonbib_data)
        self.assertEqual(m.bibcode, nonbib_data['bibcode'])
        self.assertAlmostEqual(m.boost, nonbib_data['boost'], places=5)
        self.assertEqual(m.citation_count, nonbib_data['citation_count'])
        self.assertEqual(m.bibgroup, nonbib_data['bibgroup'])
        self.assertEqual(m.bibgroup_facet, nonbib_data['bibgroup_facet'])
        self.assertEqual(m.esource, nonbib_data['esource'])
        self.assertEqual(m.grants, nonbib_data['grants'])
        self.assertEqual(m.ned_objects, nonbib_data['ned_objects'])
        self.assertEqual(m.norm_cites, nonbib_data['norm_cites'])
        self.assertEqual(m.read_count, nonbib_data['read_count'])
        self.assertEqual(m.readers, nonbib_data['readers'])
        self.assertEqual(m.reference, nonbib_data['reference'])
        self.assertEqual(m.simbad_objects, nonbib_data['simbad_objects'])
        self.assertEqual(m.total_link_counts, nonbib_data['total_link_counts'])
        self.assertEqual(m.data.data, nonbib_data['data']) # data is a special field name
        self.assertAlmostEqual(m.citation_count_norm, nonbib_data['citation_count_norm'], places=5)

        for i in range(len(nonbib_data['data_links_rows'])):
            self.assertEqual(m.data_links_rows[i].link_type, nonbib_data['data_links_rows'][i]['link_type'])
            self.assertEqual(m.data_links_rows[i].link_sub_type, nonbib_data['data_links_rows'][i]['link_sub_type'])
            self.assertEqual(m.data_links_rows[i].url, nonbib_data['data_links_rows'][i]['url'])
            self.assertEqual(m.data_links_rows[i].title, nonbib_data['data_links_rows'][i]['title'])
            self.assertEqual(m.data_links_rows[i].item_count, nonbib_data['data_links_rows'][i]['item_count'])


    def test_datalinks(self):
        """test creation of protobuf

        should include at least all fields listed AdsDataSqlSync:adsdata/run.py:nonbib_to_master_fields"""
        datalinks_data = {'bibcode': '2003ASPC..295..361M',
                          'data_links_rows': [{'link_type': 'a', 'link_sub_type': 'b',
                                               'url': ['http://a', 'http://b'],
                                               'title': ['x', 'y'],
                                               'item_count':1},
                                              {'link_type': 'aa', 'link_sub_type': 'bb',
                                               'url': ['http://aa', 'http://bb'],
                                               'title': ['xx', 'yy'],
                                               'item_count':2}]
                          }
        m = DataLinksRecord(**datalinks_data)
        self.assertEqual(m.bibcode, datalinks_data['bibcode'])

        for i in range(len(datalinks_data['data_links_rows'])):
            self.assertEqual(m.data_links_rows[i].link_type, datalinks_data['data_links_rows'][i]['link_type'])
            self.assertEqual(m.data_links_rows[i].link_sub_type, datalinks_data['data_links_rows'][i]['link_sub_type'])
            self.assertEqual(m.data_links_rows[i].url, datalinks_data['data_links_rows'][i]['url'])
            self.assertEqual(m.data_links_rows[i].title, datalinks_data['data_links_rows'][i]['title'])
            self.assertEqual(m.data_links_rows[i].item_count, datalinks_data['data_links_rows'][i]['item_count'])


    def test_datalinks_list(self):
        datalinks_list = {
            'status': 2,    #name='new', index=2, number=2,
            'datalinks_records':[{'bibcode': '2013MNRAS.435.1904M',
                                  'data_links_rows': [{'link_type': 'ESOURCE', 'link_sub_type': 'EPRINT_HTML',
                                         'url': ['http://arxiv.org/abs/1307.6556'], 'title': [''], 'item_count':0},
                                        {'link_type': 'ESOURCE', 'link_sub_type': 'EPRINT_PDF',
                                         'url': ['http://arxiv.org/pdf/1307.6556'], 'title': [''], 'item_count':0},
                                        {'link_type': 'ESOURCE', 'link_sub_type': 'PUB_HTML',
                                         'url': ['http://dx.doi.org/10.1093%2Fmnras%2Fstt1379'], 'title': [''], 'item_count':0},
                                        {'link_type': 'ESOURCE', 'link_sub_type': 'PUB_PDF',
                                         'url': ['http://mnras.oxfordjournals.org/content/435/3/1904.full.pdf'], 'title': [''], 'item_count':0}]},
                                 {'bibcode': '2013MNRAS.435.1904M',
                                  'data_links_rows': [{'link_type': 'DATA', 'link_sub_type': 'CXO',
                                         'url': ['http://cda.harvard.edu/chaser?obsid=494'], 'title': ['Chandra Data Archive ObsIds 494'], 'item_count':27},
                                        {'link_type': 'DATA', 'link_sub_type': 'ESA',
                                         'url': ['http://archives.esac.esa.int/ehst/#bibcode=2013MNRAS.435.1904M'], 'title': ['European HST References (EHST)'], 'item_count':1},
                                        {'link_type': 'DATA', 'link_sub_type': 'HEASARC',
                                         'url': ['http://heasarc.gsfc.nasa.gov/cgi-bin/W3Browse/biblink.pl?code=2013MNRAS.435.1904M'], 'title': ['s'], 'item_count':1},
                                        {'link_type': 'DATA', 'link_sub_type': 'Herschel',
                                         'url': ['http://herschel.esac.esa.int/hpt/publicationdetailsview.do?bibcode=2013MNRAS.435.1904M'], 'title': ['s'], 'item_count':1},
                                        {'link_type': 'DATA', 'link_sub_type': 'NED',
                                         'url': ['http://$NED$/cgi-bin/nph-objsearch?search_type=Search&refcode=2013MNRAS.435.1904M'], 'title': ['NED Objects (1)'], 'item_count':1},
                                        {'link_type': 'DATA', 'link_sub_type': 'SIMBAD',
                                         'url': ['http://$SIMBAD$/simbo.pl?bibcode=2013MNRAS.435.1904M'], 'title': ['SIMBAD Objects (30)'], 'item_count':30},
                                        {'link_type': 'DATA', 'link_sub_type': 'XMM',
                                         'url': ['http://nxsa.esac.esa.int/nxsa-web/#obsid=0097820101'], 'title': ['XMM-Newton Observation Number 0097820101'], 'item_count':1}]},
                                 {'bibcode': '2017MNRAS.467.3556B',
                                  'data_links_rows': [
                                        {'link_type': 'PRESENTATION',  'link_sub_type': '',
                                         'url': ['1971ATsir.615....4D', '1974Afz....10..315D', '1971ATsir.621....7D',
                                                 '1976Afz....12..665D', '1971ATsir.624....1D', '1983Afz....19..229D',
                                                 '1983Ap.....19..134D', '1973ATsir.759....6D', '1984Afz....20..525D',
                                                 '1984Ap.....20..290D', '1974ATsir.809....1D', '1974ATsir.809....2D',
                                                 '1974ATsir.837....2D'],
                                         'title': ['Part  1', 'Part  2', 'Part  3', 'Part  4', 'Part  5', 'Part  6', 'Part  7',
                                                   'Part  8', 'Part  9', 'Part 10', 'Part 11', 'Part 12', 'Part 13'],
                                         'item_count':0}]}]
        }
        m = DataLinksRecordList()
        m.status = datalinks_list['status']
        for datalinks_record in datalinks_list['datalinks_records']:
            m.datalinks_records.add(**datalinks_record)

        self.assertEqual(m.status, datalinks_list['status'])
        for i in range(len(datalinks_list['datalinks_records'])):
            self.assertEqual(m.datalinks_records[i].bibcode, datalinks_list['datalinks_records'][i]['bibcode'])
            for j in range (len(datalinks_list['datalinks_records'][i]['data_links_rows'])):
                self.assertEqual(m.datalinks_records[i].data_links_rows[j].link_type,
                                 datalinks_list['datalinks_records'][i]['data_links_rows'][j]['link_type'])
                self.assertEqual(m.datalinks_records[i].data_links_rows[j].link_sub_type,
                                 datalinks_list['datalinks_records'][i]['data_links_rows'][j]['link_sub_type'])
                self.assertEqual(m.datalinks_records[i].data_links_rows[j].url,
                                 datalinks_list['datalinks_records'][i]['data_links_rows'][j]['url'])
                self.assertEqual(m.datalinks_records[i].data_links_rows[j].title,
                                 datalinks_list['datalinks_records'][i]['data_links_rows'][j]['title'])
                self.assertEqual(m.datalinks_records[i].data_links_rows[j].item_count,
                                 datalinks_list['datalinks_records'][i]['data_links_rows'][j]['item_count'])


    def test_document_record(self):
        """test creation of protobuf

        should include at least all fields listed AdsDataSqlSync:adsdata/run.py:nonbib_to_master_fields"""
        document_record = {
                            'bibcode': '2021ApJ...913L...7A',
                            'identifier': ['2021ApJ...913L...7A', '2020arXiv201014533T'],
                            'links': {
                                'DOI': '10.3847/2041-8213/abe949',
                                'ARXIV': 'arXiv:2010.14533',
                                'DATA': [
                                    {'type': 'SIMBAD', 'url': ['http://simbad.u-strasbg.fr/simbo.pl?bibcode=2021ApJ...913L...7A'],
                                     'title': ['http://simbad.u-strasbg.fr/simbo.pl?bibcode=2021ApJ...913L...7A'], 'count': 15}
                                ],
                                'ESOURCE': [
                                    {'type': 'EPRINT_HTML', 'url': ['https://arxiv.org/abs/2010.14533'],
                                     'title': ['https://arxiv.org/abs/2010.14533']},
                                    {'type': 'EPRINT_PDF', 'url': ['https://arxiv.org/pdf/2010.14533'],
                                     'title': ['https://arxiv.org/pdf/2010.14533']},
                                    {'type': 'PUB_HTML', 'url': ['https://doi.org/10.3847%2F2041-8213%2Fabe949'],
                                     'title': ['https://doi.org/10.3847%2F2041-8213%2Fabe949']},
                                    {'type': 'PUB_PDF', 'url': ['http://iopscience.iop.org/article/10.3847/2041-8213/abe949/pdf'],
                                     'title': ['http://iopscience.iop.org/article/10.3847/2041-8213/abe949/pdf']}
                                ],
                                'ASSOCIATED': {'url': ['2021ApJ...913L...7A', '2021nova.pres.7954K'],
                                               'title': ['Main Paper', 'Press Release']},
                                'CITATIONS': 'True',
                                'REFERENCES': 'True'}
                        }
        m = DocumentRecord(**document_record)
        self.assertEqual(m.bibcode, document_record['bibcode'])
        self.assertEqual(m.identifier, document_record['identifier'])
        self.assertEqual(json_format.MessageToDict(m.links), document_record['links'])

    def test_document_records(self):
        """test creation of protobuf"""

        document_records = {
            'status': 2,    #name='new', index=2, number=2,
            'document_records':[
                {
                    'bibcode': '2021ApJ...913L...7A',
                    'identifier': ['2021ApJ...913L...7A', '2020arXiv201014533T'],
                    'links': {
                        'DOI': '10.3847/2041-8213/abe949',
                        'ARXIV': 'arXiv:2010.14533',
                        'DATA': [
                            {'type': 'SIMBAD',
                             'url': ['http://simbad.u-strasbg.fr/simbo.pl?bibcode=2021ApJ...913L...7A'],
                             'title': ['http://simbad.u-strasbg.fr/simbo.pl?bibcode=2021ApJ...913L...7A'], 'count': 15}
                        ],
                        'ESOURCE': [
                            {'type': 'EPRINT_HTML', 'url': ['https://arxiv.org/abs/2010.14533'],
                             'title': ['https://arxiv.org/abs/2010.14533']},
                            {'type': 'EPRINT_PDF', 'url': ['https://arxiv.org/pdf/2010.14533'],
                             'title': ['https://arxiv.org/pdf/2010.14533']},
                            {'type': 'PUB_HTML', 'url': ['https://doi.org/10.3847%2F2041-8213%2Fabe949'],
                             'title': ['https://doi.org/10.3847%2F2041-8213%2Fabe949']},
                            {'type': 'PUB_PDF',
                             'url': ['http://iopscience.iop.org/article/10.3847/2041-8213/abe949/pdf'],
                             'title': ['http://iopscience.iop.org/article/10.3847/2041-8213/abe949/pdf']}
                        ],
                        'ASSOCIATED': {'url': ['2021ApJ...913L...7A', '2021nova.pres.7954K'],
                                       'title': ['Main Paper', 'Press Release']},
                        'CITATIONS': 'True',
                        'REFERENCES': 'True'}
                }, {
                    'bibcode': '2012Sci...338..355D',
                    'identifier': ['2012Sci...338..355D', '2012arXiv1210.6132D'],
                    'links': {
                        'DOI': '10.1126/science.1224768',
                        'ARXIV': 'arXiv:1210.6132',
                        'DATA': [
                            {'type': 'CDS', 'url': ['http://vizier.u-strasbg.fr/viz-bin/cat/J/other/Sci/338.355'],
                             'title': ['http://vizier.u-strasbg.fr/viz-bin/cat/J/other/Sci/338.355'], 'count': 1},
                            {'type': 'SIMBAD',
                             'url': ['http://simbad.u-strasbg.fr/simbo.pl?bibcode=2012Sci...338..355D'],
                             'title': ['http://simbad.u-strasbg.fr/simbo.pl?bibcode=2012Sci...338..355D'], 'count': 2}
                        ],
                        'ESOURCE': [
                            {'type': 'EPRINT_HTML', 'url': ['https://arxiv.org/abs/1210.6132'],
                             'title': ['https://arxiv.org/abs/1210.6132']},
                            {'type': 'EPRINT_PDF', 'url': ['https://arxiv.org/pdf/1210.6132'],
                             'title': ['https://arxiv.org/pdf/1210.6132']},
                            {'type': 'PUB_HTML', 'url': ['http://www.sciencemag.org/cgi/content/full/338/6105/355'],
                             'title': ['http://www.sciencemag.org/cgi/content/full/338/6105/355']},
                            {'type': 'PUB_PDF', 'url': ['http://www.sciencemag.org/content/338/6105/355.full'],
                             'title': ['http://www.sciencemag.org/content/338/6105/355.full']}
                        ],
                        'ASSOCIATED': {'url': ['2012yCatp021033801D', '2012Sci...338..355D', '2012Sci...338..355D'],
                                       'title': ['Catalog Description', 'Source Paper', 'Supporting Media']},
                        'PRESENTATION': {'url': ['http://www.youtube.com/watch?v=323IIht3Jpg']}}
                }
            ]
        }

        n = DocumentRecords(**document_records)
        self.assertEqual(n.status, document_records['status'])
        for i, document_record in enumerate(document_records['document_records']):
            self.assertEqual(n.document_records[i].bibcode, document_record['bibcode'])
            self.assertEqual(n.document_records[i].identifier, document_record['identifier'])
            self.assertEqual(json_format.MessageToDict(n.document_records[i].links), document_record['links'])


    def test_data_source(self):
        """test creation of protobuf

        should include at least all fields listed AdsDataSqlSync:adsdata/run.py:nonbib_to_master_fields"""
        data_source = {
            'id': 'SIMBAD',
            'name': 'SIMBAD Database at the CDS',
            'url': 'http://simbad.u-strasbg.fr',
        }
        m = DataSource(**data_source)
        self.assertEqual(m.name, data_source['name'])
        self.assertEqual(m.url, data_source['url'])

    def test_data_source_list(self):
        """test creation of protobuf"""

        data_source_list = {
            'status': 2,    #name='new', index=2, number=2,
            'data_source':[
                {
                    'id': 'SIMBAD',
                    'name': 'SIMBAD Database at the CDS',
                    'url': 'http://simbad.u-strasbg.fr',
                }, {
                    'id': 'XMM',
                    'name': 'XMM Newton Science Archive',
                    'url': 'http://nxsa.esac.esa.int',
                }, {
                    'id': 'NED',
                    'name': 'NASA/IPAC Extragalactic Database',
                    'url': 'https://ned.ipac.caltech.edu',
                }
            ]
        }

        n = DataSourceList(**data_source_list)
        self.assertEqual(n.status, data_source_list['status'])
        for i, data_source in enumerate(data_source_list['data_source']):
            self.assertEqual(n.data_source[i].id, data_source['id'])
            self.assertEqual(n.data_source[i].name, data_source['name'])
            self.assertEqual(n.data_source[i].url, data_source['url'])


if __name__ == '__main__':
    unittest.main()
