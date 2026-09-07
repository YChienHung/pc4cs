---
title: 'People'
type: landing

design:
  spacing: '5rem'

sections:
  - block: team-showcase
    content:
      title: Meet Our Team
      subtitle: World-class researchers advancing science
      text: Our diverse team brings together expertise from multiple disciplines.
      user_groups:
        - Principal Investigators
        - Assistant Researchers
        - Postdoctoral Researchers
        - Administrative Assistants
        - PhD Students
        - Undergraduate Interns
        - name: Alumni          # optional per-group sort override
          sort_by: graduation_year
          sort_ascending: false
      sort_by: 'graduation_year' # legacy 'Params.' prefix optional
      sort_ascending: false
      # cta:
      #   text: Join Our Team
      #   url: /opportunities
      #   icon: user-plus
    design:
      show_role: true
      show_organizations: false
      show_interests: true
      max_interests: 3   # set 0 to hide interests even if provided
      align: center      # or "left" to align header + CTA left
      max_columns: 4     # 2, 3, or 4
      show_social: true
      show_empty_groups: false # show a placeholder when a group has no members
      # Section background color (CSS class)
      css_class: "bg-gray-50 dark:bg-gray-900 team-round-avatars"

---