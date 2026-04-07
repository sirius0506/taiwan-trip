import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx_flights = content.find("<!-- FLIGHTS -->")
idx_hotel = content.find("<!-- HOTEL -->")
idx_itinerary = content.find("<!-- ITINERARY -->")
idx_budget = content.find("<!-- BUDGET -->")

if idx_flights == -1 or idx_hotel == -1 or idx_itinerary == -1 or idx_budget == -1:
    print("Error finding markers")
    sys.exit(1)

part1 = content[:idx_flights]
flights_str = content[idx_flights:idx_hotel]
hotel_str = content[idx_hotel:idx_itinerary]
itinerary_str = content[idx_itinerary:idx_budget]
part4 = content[idx_budget:]

# 1. Update Flight header
flights_str = flights_str.replace(
    '김포 → 송산 오전 직항편만 선별했습니다. 4월 8일(수) 기준 비교입니다.',
    '회원님이 확정하신 이스타항공편 일정 및 기타 참고용 비교 리스트입니다.'
)

# 2. Remove 'recommended' from EVA
flights_str = flights_str.replace('<div class="flight-card recommended animate-on-scroll">', '<div class="flight-card animate-on-scroll">')
flights_str = flights_str.replace('      <div class="flight-badge">추천</div>\n', '')

# 3. Add 'recommended' and '확정' badge to Eastar
old_eastar = '<div class="flight-card animate-on-scroll">\n      <div class="flight-airline">🟠 이스타항공 (ZE)</div>'
new_eastar = '<div class="flight-card recommended animate-on-scroll">\n      <div class="flight-badge" style="background:var(--accent-coral); color:white;">확정</div>\n      <div class="flight-airline">🟠 이스타항공 (ZE)</div>'
flights_str = flights_str.replace(old_eastar, new_eastar)

# Reorder: OVERVIEW (in part1) -> ITINERARY -> FLIGHTS -> HOTEL -> BUDGET (in part4)
new_content = part1 + itinerary_str + flights_str + hotel_str + part4

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
    
print("Reorder successful!")
