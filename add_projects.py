import re

def create_item(name, slug, category, year="2025"):
    return f'''              <div role="listitem" class="w-dyn-item"><a data-w-id="a35537f9-ade8-dabb-e2f1-3a6e0e267bea"
                  href="projects/{slug}.html" class="index1_item w-inline-block">
                  <div class="w-layout-grid grid-global is-row0">
                    <div id="w-node-a35537f9-ade8-dabb-e2f1-3a6e0e267bec-eef82a0c">
                      <div>{name}</div>
                    </div>
                    <div id="w-node-a35537f9-ade8-dabb-e2f1-3a6e0e267bee-eef82a0c">
                      <div class="color_muted1">{category}</div>
                    </div>
                    <div id="w-node-a35537f9-ade8-dabb-e2f1-3a6e0e267bf0-eef82a0c"
                      class="w-layout-hflex flex-h_spacebetween">
                      <div class="color_muted1">{year}</div>
                      <div class="hide_tablet">
                        <div id="w-node-_4ac37994-fc5a-8048-3c1f-3a06853e9b44-853e9b44" class="cta-circle">
                          <div class="cta-circle_bg"></div>
                          <div class="cta-circle_arrow-wrap">
                            <div class="cta-circle_arrow w-embed"><svg xmlns="http://www.w3.org/2000/svg"
                                viewbox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                                stroke-linecap="square" stroke-linejoin="square">
                                <line x1="5" y1="12" x2="19" y2="12"></line>
                                <polyline points="12 5 19 12 12 19"></polyline>
                              </svg></div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </a></div>'''

new_items = [
    create_item("Cloud Ledger", "cloud-ledger", "Accounting & Finance Software"),
    create_item("Crew Hive", "crew-hive", "Workforce Management App"),
    create_item("E-Jamaath", "ejamaath", "Community Management App"),
    create_item("Hudaibiyya", "hudaibiyya", "Business Website"),
    create_item("Revops AI", "revops-ai", "Revenue Operations Software")
]

# 1. Update work-index.html
with open('work-index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the end of the list (right after kkmuttonstall)
target = 'href="projects/kkmuttonstall.html"'
idx = content.find(target)
if idx != -1:
    end_of_kkmuttonstall = content.find('</a></div>', idx) + 10
    # Insert new items here
    combined_new = '\n'.join(new_items)
    content = content[:end_of_kkmuttonstall] + '\n' + combined_new + content[end_of_kkmuttonstall:]

    with open('work-index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated work-index.html")

# 2. Update work-industry.html to have the exact same list
with open('work-industry.html', 'r', encoding='utf-8') as f:
    industry_content = f.read()

# We want to replace the list in work-industry.html with the list from work-index.html
# The list in work-index.html starts with <div class="w-dyn-list"> right under <div data-wf--spacing--variant="40" class="spacing w-variant-7c3405ee-7b01-c5c9-ee04-dd9e21b17e5c"></div>
list_start = content.find('<div class="w-dyn-list">')
list_end = content.find('<div data-wf--spacing--variant="custom-2"', list_start)
list_html = content[list_start:list_end]

ind_list_start = industry_content.find('<div class="w-dyn-list">')
ind_list_end = industry_content.find('<div data-wf--spacing--variant="custom-2"', ind_list_start)

if ind_list_start != -1 and ind_list_end != -1:
    industry_content = industry_content[:ind_list_start] + list_html + industry_content[ind_list_end:]
    with open('work-industry.html', 'w', encoding='utf-8') as f:
        f.write(industry_content)
    print("Updated work-industry.html with the copied list from work-index.html")
else:
    print("Could not find the target section in work-industry.html")
