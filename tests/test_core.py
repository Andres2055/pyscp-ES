#!/usr/bin/env python3

###############################################################################
# Module Imports
###############################################################################

from pyscp.core import WikidotConnector, SnapshotConnector
import pytest
import random

###############################################################################

DBPATH = '/home/anqxyr/heap/_scp/scp-wiki.2015-03-16.db'
USERNAME = 'andres205'
PASSWORD = ("""morrocoy""")


@pytest.mark.parametrize('cn', [
    WikidotConnector('www.lafundacionscp.wikidot.com'),
    SnapshotConnector('www.lafundacionscp.wikidot.com', DBPATH)])
class TestSCPWikiConnectors:

    def test_revision(self, cn):
        revision = cn('scp-es-040').history[0]
        assert revision.revision_id == 39167223
        assert revision.page_id == 18578010
        assert revision.number == 0
        assert revision.user == 'andres2055'
        assert revision.time == '2013-06-30 16:34:37'
        assert revision.comment == 'INICIADA LA RUTINA DE VENIDA'

    def test_post(self, cn):
        post = cn('scp-es-040').comments[0]
        assert post.post_id == 1806664
        assert post.thread_id == 666715
        assert post.parent is None
        assert post.title is None
        assert post.user == 'FlameShirt'
        assert post.time == '2013-06-30 16:47:22'
        assert post.wordcount == 26

    def test_list_pages(self, cn):
        pages = list(cn.list_pages(author='andres2055', tag='esfera'))
        assert pages == ['www.lafundacionscp.wikidot.com/scp-es-050']

    def test_list_pages_rewrites(self, cn):
        pages = list(cn.list_pages(author='Mulnero', tag='es'))
        assert 'www.lafundacionscp.wikidot.com/scp-es-099' in pages


class TestActiveMethods:

    @pytest.fixture
    def wiki(self, cache=[]):
        if cache:
            return cache[0]
        if not USERNAME or not PASSWORD:
            pytest.skip('necesita datos de autenticación')
        wiki = WikidotConnector('wikitest2')
        wiki.auth(USERNAME, PASSWORD)
        cache.append(wiki)
        return wiki

    def test_edit_page(self, wiki):
        value = random.randint(0, 1000000)
        p = wiki('page1')
        p.edit(value, comment='testeo automatizado')
        assert p.source == str(value)

    def test_revert(self, wiki):
        p = wiki('page1')
        p.revert_to(24)
        assert p.source == 'no hay dirección aquí'

    def test_set_tags(self, wiki):
        value = random.randint(0, 1000000)
        p = wiki('page1')
        p.set_tags(p.tags + [str(value)])
        assert str(value) in p.tags


if __name__ == '__main__':
    pytest.main()
