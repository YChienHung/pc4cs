---
title: '项目'
type: landing

# Page sections
sections:
  - block: portfolio
    id: projects
    content:
      title: 代表项目
      text: 这里展示了我参与的部分研究与实践项目，涵盖科研探索、技术开发与实际应用。
      count: 0
      filters:
        folders:
          - projects
      buttons:
        - name: All
          tag: '*'
        - name: Full-Stack
          tag: Full-Stack
        - name: Frontend
          tag: Frontend
        - name: Backend
          tag: Backend
      default_button_index: 0
      # Archive link auto-shown if more projects exist than 'count' above
      # archive:
      #   enable: false  # Set to false to explicitly hide
      #   text: "Browse All"  # Customize text
      #   link: "/work/"  # Custom URL
    design:
      columns: 3
      background:
        color:
          light: "#ffffff"
          dark: "#0d0d12"
      spacing:
        padding: ["4rem", "0", "4rem", "0"]
  - block: cta-image-paragraph
    id: solutions
    content:
      items:
        - title: Built for makers shipping fast
          text: Beacon meets you where your customers already are. Drop in the widget, sync your tools, and watch themes emerge in your first week.
          feature_icon: check
          features:
            - "One-line install (JS snippet or SDK)"
            - "30+ integrations out of the box"
            - "AI synthesis from day one"
          # Pexels — Rodrigo Santos / photo 3888151 (free for commercial use)
          image: makers-shipping.jpg
          button:
            text: Start free
            url: "#pricing"
        - title: Loved by product and support teams
          text: Bring product, support, and engineering to the same table. Beacon turns scattered feedback into shared truth — backed by data, not opinions.
          feature_icon: bolt
          features:
            - "Slack, Zendesk, Intercom, and Linear sync"
            - "Custom roles, audit logs, and SSO"
            - "Round-trip roadmap status updates"
          # Pexels — Anna Shvets / photo 5716018 (free for commercial use)
          image: teams-collaboration.jpg
          button:
            text: Book a demo
            url: "https://beacon.example.com/demo"
    design:
      # Section background color (CSS class)
      css_class: "bg-gray-100 dark:bg-gray-900"
  - block: logos
    content:
      title: Trusted by product teams at
      items:
        - icon: brands/github
          name: GitHub
        - icon: brands/google
          name: Google
        - icon: brands/microsoft
          name: Microsoft
        - icon: brands/nvidia
          name: NVIDIA
        - icon: brands/openai
          name: OpenAI
        - icon: brands/anthropic
          name: Anthropic
        - icon: brands/stripe
          name: Stripe
        - icon: brands/vercel
          name: Vercel
    design:
      layout: marquee
      # White logos read cleanly against the dark band; both styles work — see logos block schema
      logo_style: white
      logo_size: md
      marquee_speed: 35
      # `dark` activates child components' `dark:` variants, `bg-gray-900` paints the band.
      # Extends the dark zone from the hero, so the hero's fade-bottom no longer reveals a light strip.
      css_class: "dark bg-gray-900"
      spacing:
        padding: ["2rem", 0, "2rem", 0]

---
