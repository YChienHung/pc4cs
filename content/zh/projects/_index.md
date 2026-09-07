---
title: '项目'
type: landing

# Page sections
sections:
  - block: collection
    content:
      title: Selected Projects
      text: I enjoy making things. Here are a selection of projects that I have worked on over the years.
      filters:
        folders:
          - projects
    design:
      view: article-grid
      fill_image: false
      columns: 3
      show_date: false
      show_read_time: false
      show_read_more: false
      
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
