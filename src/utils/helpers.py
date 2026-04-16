
def pagination(query, page: int = 1, limit: int = 10):
    total = query.count()
    total_pages = (total + limit - 1) // limit

    results = query.offset((page - 1) * limit).limit(limit).all()

    return {
        "total": total,
        "page": page,
        "limit": limit,
        "total_pages": total_pages,
        "data": results
    }