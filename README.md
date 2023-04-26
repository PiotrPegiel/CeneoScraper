# CeneoScraper
## Selektory składowych opinii w Ceneo.pl
| Składowa | Nazwa | selektor                                                           |
| --- | --- |--------------------------------------------------------------------|
| identyfikator opinii | opinion\_id | [data-entry-id]                                                    |
| autora | author | span.user-post\_\_author-name                                      |
| rekomendację | recommendation | span.user-post\_\_author-recomendation \> em                       |
| liczbę gwiazdek | rating | span. user-post\_\_score-count                                     |
| czy opinia jest potwierdzona zakupem | verified | div.review-pz                                                      |
| data wystawienia opinii | post\_date | span.user-post\_\_published \> time:nth-child(1)[datetime]         |
| data zakupu produktu | purchase\_date | span.user-post\_\_published \> time:nth-child(2)[datetime]         |
| ile osób uznało opinię za przydatną | vote\_up | button.vote-yes[data-total-vote]  /  button.vote-yes \> span       |
| ile osób uznało opinię za nieprzydatną | vote\_down | button.vote-no[data-total-vote]  /  button.vote-no \> span         |
| treść opinii | content | div.user-post\_\_text                                              |
| listę wad | cons | div.review-feature\_\_title—negatives ~ div.review-feature\_\_item |
| listę zalet | pros | div.review-feature\_\_title—positives ~ div.review-feature\_\_item |

## Wykorzystane biblioteki
- BeautifoulSoup4
- Requests
- Json
- Os
- Pandas
- Numpy
- Matplotlib