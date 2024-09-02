select
    ape.id,
    ape.timestamp,
    a.name as astrolog_name,
    a.id as astrolog_id,
    au.astrolog_user_type
from {{ ref("raw_astrolog_ping_events") }} ape
left join {{ ref("raw_astrolog_user_ref") }} au on ape.astrolog_user = au.id
left join {{ ref("raw_astrologs") }} a on au.astrolog = a.id
