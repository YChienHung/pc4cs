---
title: "团队成员"
type: landing

sections:
  - block: team-showcase
    content:
      title: 认识我们的团队
      subtitle: 汇聚优秀科研人才，探索科学前沿
      # text: 我们的团队汇聚了来自不同学科背景的研究人员，融合多领域的专业知识与研究经验，致力于推动前沿科学研究与技术创新。
      user_groups:
        - 首席研究员
        - 助理研究员
        - 博士后研究员
        - 行政助理
        - 博士研究生
        - 本科交流生
        - name: 校友 # optional per-group sort override
          sort_by: graduation_year
          sort_ascending: false
      sort_by: "graduation_year" # legacy 'Params.' prefix optional
      sort_ascending: false
      # cta:
      #   text: Join Our Team
      #   url: /opportunities
      #   icon: user-plus
    design:
      show_role: true
      show_organizations: false
      show_interests: true
      max_interests: 3 # set 0 to hide interests even if provided
      align: center # or "left" to align header + CTA left
      max_columns: 4 # 2, 3, or 4
      show_social: true
      show_empty_groups: false # show a placeholder when a group has no members
      # Section background color (CSS class)
      css_class: "team-round-avatars"
---
