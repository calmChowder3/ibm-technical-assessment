SELECT owner.owner_id, owner.owner_name, COUNT( DISTINCT category_article_mapping.category_id) as different_category_count
FROM owner
INNER JOIN article ON article.owner_id = owner.owner_id
INNER JOIN category_article_mapping ON article.article_id = category_article_mapping.article_id
GROUP BY owner.owner_id
ORDER BY different_category_count DESC;