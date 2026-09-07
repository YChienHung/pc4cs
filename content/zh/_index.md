---
# Leave the homepage title empty to use the site title
title: "首页"
type: landing

sections:
  - block: main-gallery
    content:
      items:
        - src: main/1.jpg
          caption: The **main workspace** where most of our research happens
          credit: "Photo: [Jane Doe](https://janedoe.com)"
        - src: main/2.jpg
          title: Annual retreat
          caption: "*Edinburgh, 2024* — three days of deep work and walks"
          link: /news/retreat-2024/
        - src: main/3.jpg
          title: Annual retreat
          caption: "*Edinburgh, 2024* — three days of deep work and walks"
          link: /news/retreat-2024/
    design:
      row_height: 1000
      caption_position: overlay
      indicator_position: overlay
      edge_fade: true
      edge_fade_width: 10
      aspect_ratio: wide
      autoplay: true
      autoplay_interval: 5000
      spacing:
        padding: ["0", "0", "2rem", "0"]
  - block: hero
    content:
      eyebrow: Beacon for product teams
      title: Turn customer [noise] into your roadmap
      text: Capture feedback from every channel — Slack, email, support, in-app — and let AI surface what matters.
      primary_action:
        text: Start free
        url: "#pricing"
        icon: rocket-launch
        style: gradient
      secondary_action:
        text: How it works
        url: "#how-it-works"
        icon: play-circle
        style: ghost
      announcement:
        badge:
          text: NEW
          color: primary
        text: AI roadmap pull is live.
        link:
          text: Read more
          url: "#features"
      trust:
        stars: 5
        text: "**4.9/5** from 1,200+ product teams"
      # To switch to a split layout with a product mockup, uncomment the media block
      # below and set `design.layout: split-left` (or `split-right` / `stacked`):
      # media:
      #   type: image
      #   src: dashboard.png
      #   dark_src: dashboard-dark.png   # optional dark-mode variant
      #   alt: Beacon dashboard
    design:
      spacing:
        padding: [0, 0, 0, 0]
        margin: [0, 0, 0, 0]
      css_class: "dark"
      section_break:
        # Fade the hero's bottom edge into the dark logos band beneath (matches its bg-gray-900)
        fade_bottom: "#101828"
      background:
        # Deep navy base; radial glow paints a soft violet spotlight from above
        color: "#0a0e27"
        gradient:
          type: radial
          start: "rgba(124,58,237,0.45)"
          end: "transparent"
          position: "50% -10%"
          shape: ellipse
          size: "80% 80%"
        # Mesh orbs add depth and atmosphere on top of the radial glow
        gradient_mesh:
          enable: true
          style: orbs
          intensity: medium
          animation: pulse
          colors: ["primary-500/25", "secondary-500/25"]
          orb_count: 2
          positions: ["top-1/3 left-1/4", "bottom-1/3 right-1/4"]
          sizes: ["w-[32rem] h-[32rem]", "w-[26rem] h-[26rem]"]
  - block: cta-image-paragraph
    content:
      items:
        - title: Ship polished docs with Hugo Blox
          text: Pair Markdown content with responsive imagery and reusable CTAs.
          image: screenshots/docs.png
          feature_icon: hero/check-circle
          features:
            - Responsive images generated automatically
            - Markdown-first authoring
            - Works with Netlify, Vercel, and GitHub Pages
          button:
            text: Read the guide
            url: /docs/get-started/
        - title: Launch production-ready marketing pages
          text: Use alternating layouts to highlight product benefits.
          image: screenshots/marketing.png

  - block: markdown
    content:
      title: "📚 My Research"
      subtitle: ""
      text: |-
        Use this area to speak to your mission. I'm a research scientist in the Moonshot team at DeepMind. I blog about machine learning, deep learning, and moonshots.

        I apply a range of qualitative and quantitative methods to comprehensively investigate the role of science and technology in the economy.

        Please reach out to collaborate 😃
    design:
      columns: "1"
  - block: collection
    id: news
    content:
      title: Recent News
      subtitle: ""
      text: ""
      # Page type to display. E.g. post, talk, publication...
      page_type: news
      # Choose how many pages you would like to display (0 = all pages)

      count: 3
      sort_by: Date
      sort_ascending: false
      filters:
        folders:
          - news
      offset: 0
      # Page order: descending (desc) or ascending (asc) date.
      order: desc
    design:
      # Choose a layout view
      view: date-title-summary
      # Reduce spacing
      spacing:
        padding: [0, 0, 0, 0]
      fill_image: true
      show_date: true
      show_read_time: true
      show_read_more: true
---
