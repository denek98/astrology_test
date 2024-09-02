with
    astrolog_daily_ping_amount as (
        select astrolog_id, astrolog_name, count(id) as ping_amount
        from {{ ref("int_astrolog_ping_event_extended") }}
        group by astrolog_id, astrolog_name
    ),
    astrolog_daily_chat_from_ping_amount as (
        select
            a.id as astrolog_id,
            a.name as astrolog_name,
            count(ce.id) as chat_fromping_amount
        from {{ ref("raw_chat_events") }} ce
        left join {{ ref("raw_astrologs") }} a on ce.astrolog = a.id
        where ping_event is not null
        group by astrolog_id, astrolog_name
    )

select
    apa.astrolog_id,
    apa.astrolog_name,
    sum(acpa.chat_fromping_amount) * 1.0 / sum(apa.ping_amount) as conversion_rate
from astrolog_daily_ping_amount apa
left join
    astrolog_daily_chat_from_ping_amount acpa
    on apa.astrolog_id = acpa.astrolog_id
    and apa.astrolog_name = acpa.astrolog_name
group by apa.astrolog_id, apa.astrolog_name
