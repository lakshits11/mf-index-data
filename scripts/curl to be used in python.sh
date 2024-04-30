curl --compressed --location 'https://www.niftyindices.com/Backpage.aspx/getTotalReturnIndexString' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0' \
--header 'Accept: application/json, text/javascript, */*; q=0.01' \
--header 'Accept-Language: en-US,en;q=0.5' \
--header 'Accept-Encoding: gzip, deflate, br' \
--header 'Content-Type: application/json; charset=utf-8' \
--header 'X-Requested-With: XMLHttpRequest' \
--header 'Origin: https://www.niftyindices.com' \
--header 'Connection: keep-alive' \
--header 'Referer: https://www.niftyindices.com/reports/historical-data' \
--header 'Cookie: ak_bmsc=45E9AF62AA9E243367D4BA7C2F405CDC~000000000000000000000000000000~YAAQFjkgF1ETJBePAQAAP99yLRfjbL2cikQLewENrrJ3hp7T7rvXJoyXTx6h0BoDMCTHWdUEQcD2igPY4nMP1rCLrps/V14lMeXnHK3dIixUKYyrQhJN6m16ciz//+y0j+lwwbpoyhNsEs9mSaWXFBsaQtMww3zkFrBLBbgmW3/HjEP1CykcrvR/stXs+eEMajwzzXpfGA+1YAv8X86F7TSl90x607eczPcqa+jnIfP8+3hwyd0o+AXZFBB01opyqQZoADREm/yx7zs4cQxEicp+U3aKm6zjys3uHSmyDoSPRmyqwIHzhlrLknGsAr2bHZ/qzyo8CDQPQDUH9Jg6GHw041MC9AhMXP3hvZ8gTG61BKPwVdnCSz8+n7EVNBXsbUe03dE=; ASP.NET_SessionId=er5k0hx30ujw13dtphywgs32; bm_sv=5CFA5373F4070A41AD097C6C084A4D69~YAAQFjkgF3ytJBePAQAAiih3LRcXOzEy3MWfL0NCEBf79mEcNl+Ed5lqhbc24tc+14mjeIUusk7E9TsDze/E8rv3sMLK+P5G6GCaZCdB2bvmNHS6PLKnqGdk7DHONfdnaOJmTojge1gEalIz1rxGMJAm3yitl0yGY5tLzD3OOa61gnFxL5piVy3sqsL9m13Ahbc96Mu0Jmk+KUkLmtmnrpAOtROt0UxVzj8Y8CF6ucgANtVAqkgn1tqm+ieBWaj619iruImbgA==~1; bm_mi=12795BBE50D0494B6093208405F12385~YAAQFjkgF/E8JBePAQAAGfJzLRde7o5X56XhggE5OwfLM3VVoyhnHcXYwYXsV89azwf0S43TgYiAgqmpvC+euH9Znt21Pob3kRZd2eavaYUhhPaAIScz7rzo6joafVRODYJ18qWvUWwvAZXyAOwZ7wWeCCjXbVt7g61HGDJ1FfX+Qgf1zYF95c9luGVNT0+aXc4mHmUYPPdrmGtkGJaa4nYFQCzpeqfVEbSIKRlqTMHDcMx0dcqraVKZJ6PbGyhpyLJAaiDL2l4MWhOErsnlwCgkkhuoBM33KSq9/Zn0830xxZbSXtRZB76L4L7NPrOHuA7U0JblSEZLAdTJWfprGTC1dki/v8rvz13Z~1; bm_sv=5CFA5373F4070A41AD097C6C084A4D69~YAAQ0YMsMU/kpueOAQAAsKB9LRflnj7DCsvSKryVuOMDT64HjiviVIOVDayCMfcbFPvw9ota3pgHzibWnOtvM3MX+WXbmYksg+g/g88FDSnZ17R59n7rN8K8/6ihMy4WPWk+yphsTwT5BgB9hOCm8q3Ujqx77Qf4HUrnLj/c8ct4GWdhW21dOQDlLBbfDTlCeVVbz5mxMOwj+aelwCKm2fZYlcBL5/P/KAvhLmQS9Lufj+PzgjT2fV0X/ajeA9vyxA22/+CYOg==~1; ak_bmsc=45E9AF62AA9E243367D4BA7C2F405CDC~000000000000000000000000000000~YAAQ0YMsMSH9pueOAQAAOQ+LLRfPM2hbWyP75a3CjqH8RlGFXRcWNz21SgRDHhN7rsjAdnHWaKWOswwKvBPLvCHzYb96deDoD1pquutJwLvXaxky09DD5kQHp8O2UOKkKwjEB1eopO8IZZX9N5h0xhq1BQtwOX3D/88yCWY5l4aIdzuDj3j2tXLJD1WHw7c/yg2DkZQRR05cvjKBxmSSh9bRlWuHP/j+pEgE3eUsr2O/Ph3dj1QCYx7YA6t8U4rjdlz9oweVOOdSg0aFCb7Os6+mZ+LDImIsXQ2zhYWw/HzAX4LpoxuPJMZovuP0NbnyJF3EI0RrXrbESJIDv8OHWOlmcXPRzQv7yyiwlphf8KZK65TJN7u9Sfpe//TPWGqN9eF+3DHqYpbUYLepHwTwJQO4; bm_sv=5CFA5373F4070A41AD097C6C084A4D69~YAAQ0YMsMSL9pueOAQAAOQ+LLRe8FMMHEbtLZZZQiecLajcw4E6HKdiDs1gtbNLezVIHx4io9f2niH+erEpYqXNFlK1RK+pi9crxM2VZk5L5urBv4W2/BKYj9Ysnu01jTIdkwPcbzzOcb6P0D+qNJ9pndOVa+EZj8w+c2jcRmlUTnEWUXDrg3xHlHFEiIVa6hzpSrL0aGaJS2rDmGLjhl0LdDVvH1xKJnAsegTnFQGtE3c/Q6tE2JynkOLGhBmYXctNTIpbfZw==~1' \
--header 'Sec-Fetch-Dest: empty' \
--header 'Sec-Fetch-Mode: cors' \
--header 'Sec-Fetch-Site: same-origin' \
--data '{
    "cinfo": "{'\''name'\'':'\''<INDEX_NAME>'\'','\''startDate'\'':'\''01-Jan-1995'\'','\''endDate'\'':'\''30-Apr-2024'\''}"
}' \
--output "../index data/<INDEX_NAME_FILE>.json"