#!/usr/bin/env python3
"""
Tag Standardization Script
Standardizes blog post tags by:
1. Converting all to lowercase
2. Adding parent category tags
3. Replacing meaningless tags with meaningful ones
"""

import re
import os
from typing import List, Set, Dict

# Define parent categories and their indicators
CATEGORIES = {
    'algorithm': ['boj', '백준', 'programmers', '프로그래머스', 'bfs', 'dfs', 'dp', 
                  '그리디', 'mst', '다익스트라', '프림', 'ccw', '분할정복', '퀵정렬', 
                  'algorithm', '알고리즘', '완전탐색', 'graph', 'tree', 'greedy'],
    'ml': ['ml', '머신러닝', 'regression', 'classification', 'clustering', 'knn', 
           'lstm', 'rnn', 'neural', 'deep', '딥러닝', 'overfitting', 'regularization', 
           'r2', 'linear', 'polynomial', '지도학습', '비지도', '모델', 'ai', '인공지능'],
    'database': ['sql', 'db', 'sqld', 'jdbc', 'window', 'cte', 'oracle', 
                 'mysql', 'postgresql', 'database', '데이터베이스', '관계', 
                 '외래키', '기본키', 'dao', 'vo'],
    'network': ['tcp', 'udp', 'http', 'dns', 'ip', 'protocol', 
                '네트워크', 'request', 'response', 'port'],
    'java': ['java', 'jvm', '자바', 'singleton', 'polymorphism'],
    'web': ['javascript', 'js', 'nodejs', 'vue', 'html', 'css', 'frontend', 
            'backend', 'api', 'mvc', 'express', 'async', 'promise'],
    'oop': ['class', 'inheritance', '상속', 'interface', 'polymorphism', 
            '객체지향', '생성자', 'constructor', '캡슐화', '추상화'],
}

# Tags to remove (meaningless prepositions, etc.)
REMOVE_TAGS = {'with', 'this'}

# Special tag replacements based on post content
TAG_REPLACEMENTS = {
    # Posts about SQL WITH clause
    ('with', 'cte'): ['sql', 'cte', 'database', 'subquery'],
    ('with', 'sql'): ['sql', 'cte', 'database'],
}


def extract_frontmatter_and_tags(content: str) -> tuple:
    """Extract YAML frontmatter and current tags from post content."""
    # Match YAML frontmatter
    match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not match:
        return None, []
    
    frontmatter = match.group(1)
    
    # Extract tags line
    tag_match = re.search(r'^tags:\s*(.+)$', frontmatter, re.MULTILINE)
    if not tag_match:
        return frontmatter, []
    
    tags_str = tag_match.group(1).strip()
    
    # Parse tags (both [a, b, c] and a b c formats)
    if tags_str.startswith('[') and tags_str.endswith(']'):
        tags_str = tags_str[1:-1]
    
    tags = [t.strip().strip('"').strip("'") for t in re.split(r'[,\s]+', tags_str) if t.strip()]
    
    return frontmatter, tags


def determine_parent_tags(current_tags: List[str]) -> Set[str]:
    """Determine which parent category tags should be added."""
    current_lower = [t.lower() for t in current_tags]
    parents = set()
    
    for parent, indicators in CATEGORIES.items():
        # Skip if parent already exists
        if parent in current_lower:
            continue
        
        # Check if any indicator matches
        for indicator in indicators:
            if any(indicator.lower() in tag.lower() for tag in current_tags):
                parents.add(parent)
                break
    
    return parents


def replace_meaningless_tags(tags: List[str], filename: str) -> List[str]:
    """Replace meaningless tags with meaningful ones based on context."""
    tags_lower = [t.lower() for t in tags]
    
    # Check for specific replacement patterns
    for pattern, replacement in TAG_REPLACEMENTS.items():
        if all(p in tags_lower for p in pattern):
            # Remove the pattern tags
            tags = [t for t in tags if t.lower() not in pattern]
            # Add replacement tags
            for new_tag in replacement:
                if new_tag not in [t.lower() for t in tags]:
                    tags.append(new_tag)
            return tags
    
    # Remove generic meaningless tags
    tags = [t for t in tags if t.lower() not in REMOVE_TAGS]
    
    return tags


def standardize_tags(tags: List[str], filename: str) -> List[str]:
    """Standardize tags: lowercase, add parents, replace meaningless."""
    # 1. Remove meaningless tags and replace with contextual ones
    tags = replace_meaningless_tags(tags, filename)
    
    # 2. Convert to lowercase
    tags = [t.lower() for t in tags]
    
    # 3. Add parent category tags
    parents = determine_parent_tags(tags)
    
    # 4. Combine and deduplicate (preserve order)
    seen = set()
    result = []
    for tag in tags + list(parents):
        if tag not in seen:
            seen.add(tag)
            result.append(tag)
    
    return result


def update_post_tags(filepath: str) -> bool:
    """Update tags in a single post file. Returns True if modified."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    frontmatter, current_tags = extract_frontmatter_and_tags(content)
    
    if not frontmatter or not current_tags:
        return False
    
    filename = os.path.basename(filepath)
    new_tags = standardize_tags(current_tags, filename)
    
    # Check if tags changed
    if current_tags == new_tags:
        return False
    
    # Format new tags
    new_tags_str = '[' + ', '.join(new_tags) + ']'
    
    # Replace tags line in frontmatter
    new_frontmatter = re.sub(
        r'^tags:\s*.+$',
        f'tags: {new_tags_str}',
        frontmatter,
        flags=re.MULTILINE
    )
    
    # Replace in content
    new_content = re.sub(
        r'^---\n.*?\n---\n',
        f'---\n{new_frontmatter}\n---\n',
        content,
        count=1,
        flags=re.DOTALL
    )
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f'✓ {filename}')
    print(f'  Before: {current_tags[:5]}{"..." if len(current_tags) > 5 else ""}')
    print(f'  After:  {new_tags[:5]}{"..." if len(new_tags) > 5 else ""}')
    
    return True


def main():
    """Main execution function."""
    posts_dir = '_posts'
    
    if not os.path.exists(posts_dir):
        print(f'Error: {posts_dir} directory not found')
        return
    
    modified_count = 0
    total_count = 0
    
    print('Starting tag standardization...\n')
    
    for filename in sorted(os.listdir(posts_dir)):
        if not filename.endswith('.md'):
            continue
        
        total_count += 1
        filepath = os.path.join(posts_dir, filename)
        
        if update_post_tags(filepath):
            modified_count += 1
            print()
    
    print(f'\nCompleted!')
    print(f'Modified: {modified_count}/{total_count} posts')


if __name__ == '__main__':
    main()
