with
    user_type_ping_amount as (
        select astrolog_user_type as user_type, count(id) as ping_amount
        from {{ ref("int_astrolog_ping_event_extended") }}
        group by user_type
    ),
    user_type_chat_from_ping_amount as (
        select ape.astrolog_user_type as user_type, count(ce.id) as chat_fromping_amount
        from {{ ref("raw_chat_events") }} ce
        left join
            {{ ref("int_astrolog_ping_event_extended") }} ape on ce.ping_event = ape.id
        where ping_event is not null
        group by user_type
    )

select
    utc.user_type,
    sum(utc.chat_fromping_amount) * 1.0 / sum(utp.ping_amount) as conversion_rate
from user_type_ping_amount utp
left join user_type_chat_from_ping_amount utc on utp.user_type = utc.user_type
group by utc.user_type
