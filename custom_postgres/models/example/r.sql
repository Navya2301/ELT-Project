{% set rating = 4.8 %}

SELECT *
FROM {{ ref('films')}}
WHERE user_rating = {{ rating}}

-- jinja implementation