import json
import logging
import azure.functions as func

def main(event: func.EventGridEvent):
    # Log thông tin sự kiện
    logging.info('Function triggered to process a message: %s', event.get_json())
    
    # Ghi log các thuộc tính chính của sự kiện
    logging.info('  Event Id = %s', event.id)
    logging.info('  Topic = %s', event.topic)
    logging.info('  Subject = %s', event.subject)
    logging.info('  Event Type = %s', event.event_type)

    # Xử lý kết quả
    result = json.dumps({
        'id': event.id,
        'data': event.get_json(),
        'topic': event.topic,
        'subject': event.subject,
        'event_type': event.event_type,
    })

    # Log kết quả
    logging.info('Python EventGrid trigger processed an event: %s', result)
