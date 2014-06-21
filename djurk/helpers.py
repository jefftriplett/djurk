#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .common import get_connection
from .models import HIT


def _update_hits(iterable, do_update_assignments=False):
    for mturk_hit in iterable:
        djurk_hit, _ = HIT.objects.get_or_create(mturk_id=mturk_hit.HITId)
        djurk_hit.update(mturk_hit=mturk_hit,
                         do_update_assignments=do_update_assignments)


def update_all_hits(do_update_assignments=False):
    """Get All HITS from Amazon"""

    connection = get_connection()
    _update_hits(connection.get_all_hits(),
                 do_update_assignments=do_update_assignments)


def update_reviewable_hits(do_update_assignments=False):
    """Get only reviewable HITS from Amazon"""

    connection = get_connection()
    _update_hits(connection.get_reviewable_hits(),
                 do_update_assignments=do_update_assignments)
