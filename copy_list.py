with open('work-index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Grab the list from work-index.html
start_marker = '<div class="w-dyn-list">'
end_marker = '<div data-wf--spacing--variant="custom-2"'

idx_start = index_content.find(start_marker)
idx_end = index_content.find(end_marker, idx_start)
list_html = index_content[idx_start:idx_end]

with open('work-industry.html', 'r', encoding='utf-8') as f:
    ind_content = f.read()

# In work-industry.html, replace the grid list
ind_start = ind_content.find('<div class="w-dyn-list">', ind_content.find('<section class="section_default">'))
ind_end = ind_content.find('<div data-wf--spacing--variant="200"', ind_start)

if ind_start != -1 and ind_end != -1:
    new_ind_content = ind_content[:ind_start] + list_html + ind_content[ind_end:]
    with open('work-industry.html', 'w', encoding='utf-8') as f:
        f.write(new_ind_content)
    print("Successfully replaced grid list in work-industry.html with text list from work-index.html")
else:
    print("Could not find the target section in work-industry.html")
