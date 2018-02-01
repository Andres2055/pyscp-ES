# pyscp-ES

*pyscp-ES is a translation of the anqxyr "pyscp" repository (https://github.com/anqxyr/pyscp).*

**pyscp-ES** es una libreria de python para interactuar con sitios webs alojados en Wikidot. La libreria está destinada principalmente para su uso por el staff administrativo del sitio web www.scp-wiki.net, y tiene una serie de características exclusivas para él. Sin embargo, la mayor parte de la funcionalidad básica debería aplicarse a cualquier sitio basado en wikidot.

## Instalación

Descargue el código actual, abra la carpeta contenedora, y ejecute el siguiente comando:

```
pip install . --user
```
Listo.

## Ejemplos

### Acceso a Páginas

```python
import pyscp

wiki = pyscp.wikidot.Wiki('www.scp-wiki.net')
p = wiki('scp-837')
print(
    '"{}" tiene un puntaje de {}, {} revisiones, y {} comentarios.'
    .format(p.title, p.rating, len(p.history), len(p.comments)))
```
```
"SCP-837: Multiplying Clay" tiene un puntaje de 108, 14 revisiones, y 54 comentarios.
```

Puedes acceder a otros sitios también:

```python
ru_wiki = pyscp.wikidot.Wiki('scpfoundation.ru')
p = ru_wiki('scp-837')
print('"{}" fue creado por {} el {}.'.format(p.title, p.author, p.created))
```
```
"SCP-837 - Глина умножения" fue creado por Gene R el 2012-12-26 11:12:13.
```

Si el sitio no utiliza un dominio personalizado, puede utilizar el nombre del sitio en lugar de la url completa. P.ej. `Wiki('scpsandbox2')` es lo mismo que `Wiki('scpsandbox2.wikidot.com')`.

### Editando Páginas

```python

wiki = pyscp.wikidot.Wiki('scpsandbox2')
wiki.auth('nombre_de_usuario_de_ejemplo', 'contraseña_de_ejemplo')
p = wiki('test')
last_revision = p.history[-1].number
p.edit(
    source='=Este es un **texto** centrado que usa la marcación de Wikidot.',
    title="puedes saltarte el título si no quieres cambiarlo.",
    #puedes omitir el comentario también, pero eso sería grosero.
    comment='probando edición automática')
print(p.text)   # vea si funcionó
p.revert(last_revision)  # devolvámoslo a lo que era.
```
```
Este es un texto centrado que usa la marcación de Wikidot.
```


### Snapshots

Cuando se trabaja con un gran número de páginas, podría ser más rápido crear un snapshot del sitio que descargar las páginas una por una. Los snapshots están optimizadas para descargar una gran cantidad de datos en el menor tiempo posible utilizando multi-hilos.

```python
import pyscp

creator = pyscp.snapshot.SnapshotCreator('www.scp-wiki.net', 'snapshot_file.db')
creator.take_snapshot(forums=False)
# ahí es donde esperaremos media hora para que termine.
```

Una vez creado un snapshot, puedes utilizar `snapshot.Wiki` para leer las páginas como en el primer ejemplo:

```python
wiki = pyscp.snapshot.Wiki('www.scp-wiki.net', 'snapshot_file.db')
p = wiki('scp-9005-2')
print(
    '"{}" tiene un puntaje de {}, fue creado por {}, y es increible.'
    .format(p.title, p.rating, p.author))
print('Otras páginas por {}:'.format(p.author))
for other in wiki.list_pages(author=p.author):
    print(
        '{} (puntaje: {}, creado el: {})'
        .format(other.title, other.rating, other.created))
```
```
Page "SCP-9005-2" tiene un puntaje de 80, fue creado por yellowdrakex, y es increiblee.
Otras páginas por yellowdrakex:
ClusterfREDACTED (puntaje: 112, creado el: 2011-10-20 18:08:49)
Dr Rights' Draft Box (puntaje: None, creado el: 2009-02-01 18:58:36)
Dr. Rights' Personal Log (puntaje: 3, creado el: 2008-11-26 23:03:27)
Dr. Rights' Personnel File (puntaje: 13, creado el: 2008-11-24 20:45:34)
Fifteen To Sixteen (puntaje: 17, creado el: 2010-02-15 05:55:58)
Great Short Story Concepts (puntaje: 1, creado el: 2010-06-03 19:26:06)
RUN AWAY FOREVURRR (puntaje: 79, creado el: 2011-10-24 16:34:23)
SCP-288: The "Stepford Marriage" Rings (puntaje: 56, creado el: 2008-11-27 07:47:01)
SCP-291: Disassembler/Reassembler (puntaje: 113, creado el: 2008-11-24 20:11:11)
...
```
