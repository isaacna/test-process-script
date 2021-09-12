#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from typing import List

from cdp_backend.pipeline.ingestion_models import (
    EventIngestionModel,
    EXAMPLE_MINIMAL_EVENT,
    Session
)


###############################################################################


def get_events(
    from_dt: datetime,
    to_dt: datetime,
    **kwargs,
) -> List[EventIngestionModel]:
    """
    Get all events for the provided timespan.

    Parameters
    ----------
    from_dt: datetime
        Datetime to start event gather from.
    to_dt: datetime
        Datetime to end event gather at.

    Returns
    -------
    events: List[EventIngestionModel]
        All events gathered that occured in the provided time range.

    Notes
    -----
    As the implimenter of the get_events function, you can choose to ignore the from_dt
    and to_dt parameters. However, they are useful for manually kicking off pipelines
    from GitHub Actions UI.
    """
    event = EXAMPLE_MINIMAL_EVENT
    event.body.description = "fjffjfjfjfj"

    video_uri = "https://samplelib.com/lib/preview/mp4/sample-5s.mp4"
    session_2 = Session(datetime(2005, 1, 13), video_uri, 0)
    event.sessions = [session_2]

    return [event]
