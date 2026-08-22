from wikidata_connector import WikidataConnector

connector = WikidataConnector()

# ========== VÍ DỤ 1: Tìm người nổi tiếng ==========
print("👤 Tìm thông tin về Albert Einstein:")
results = connector.search_entity("Albert Einstein")
if results:
    einstein_id = results[0]["id"]
    info = connector.get_basic_info(einstein_id)
    print(f"  ID: {einstein_id}")
    print(f"  Tên: {info['label']}")
    print(f"  Mô tả: {info['description']}")

# ========== VÍ DỤ 2: Tìm phim của Steven Spielberg ==========
print("\n🎬 Tìm phim của Steven Spielberg:")
spielberg_id = "Q8877"  # Steven Spielberg
sparql = """
SELECT ?filmLabel WHERE {
  ?film wdt:P57 wd:Q8877.
  ?film rdfs:label ?filmLabel.
  FILTER(LANG(?filmLabel) = "en")
}
LIMIT 10
"""
results = connector.sparql_query(sparql)
for i, result in enumerate(results, 1):
    print(f"  {i}. {result['filmLabel']['value']}")

# ========== VÍ DỤ 3: Danh sách các quốc gia châu Á ==========
print("\n🌍 Các quốc gia ở châu Á:")
sparql = """
SELECT ?countryLabel WHERE {
  ?country wdt:P30 wd:Q48;
           rdf:type wikibase:Item.
  ?country rdfs:label ?countryLabel.
  FILTER(LANG(?countryLabel) = "en")
}
LIMIT 10
"""
results = connector.sparql_query(sparql)
for result in results:
    print(f"  - {result['countryLabel']['value']}")

# ========== VÍ DỤ 4: Tìm các tác phẩm của nhà văn ==========
print("\n📚 Tác phẩm của J.K. Rowling:")
sparql = """
SELECT ?workLabel WHERE {
  ?work wdt:P50 wd:Q34661.
  ?work rdfs:label ?workLabel.
  FILTER(LANG(?workLabel) = "en")
}
LIMIT 10
"""
results = connector.sparql_query(sparql)
for i, result in enumerate(results, 1):
    print(f"  {i}. {result['workLabel']['value']}")

# ========== VÍ DỤ 5: Tìm dữ liệu về một thành phố ==========
print("\n🏙️ Thông tin về Hà Nội:")
results = connector.search_entity("Hanoi", "en")
if results:
    hanoi_id = results[0]["id"]
    info = connector.get_basic_info(hanoi_id)
    print(f"  ID: {hanoi_id}")
    print(f"  Tên: {info['label']}")
    print(f"  Mô tả: {info['description']}")
    
    # Lấy dân số
    claims = connector.get_claims(hanoi_id, "P1082")
    if claims:
        try:
            population = claims[0]["mainsnak"]["datavalue"]["value"]["amount"]
            print(f"  Dân số: {population}")
        except (KeyError, TypeError):
            print(f"  Dân số: Không có dữ liệu")
