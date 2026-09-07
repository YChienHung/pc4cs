/* 页面内筛选，不向服务器发送搜索内容；每个区块独立初始化。 */
(() => {
  const normalize = (value) =>
    String(value || "")
      .normalize("NFKC")
      .toLocaleLowerCase()
      .replace(/\s+/g, " ")
      .trim();
  // 与模板保持一致：只统一类型标识，不在脚本中维护翻译文本。
  const canonicalType = (value) => {
    const raw = normalize(value);
    return (
      {
        0: "uncat",
        1: "paper-conference",
        2: "article-journal",
        3: "article",
        4: "report",
        5: "book",
        6: "chapter",
        7: "thesis",
        8: "patent",
      }[raw] || raw
    );
  };
  function init() {
    document.querySelectorAll("[data-publication-search]").forEach((root) => {
      if (root.dataset.ready) return;
      root.dataset.ready = "true";
      const countTemplate =
        root.querySelector("[data-count]").dataset.countTemplate ||
        "{count} / {total}";
      const query = root.querySelector("[data-query]");
      const year = root.querySelector("select[data-year]");
      const type = root.querySelector("select[data-type]");
      const papers = Array.from(
        root.querySelectorAll("[data-paper]"),
        (node) => {
          let types = [];
          try {
            types = JSON.parse(node.dataset.types || "[]");
          } catch (_) {
            /* 保留条目 */
          }
          if (!Array.isArray(types)) types = [];
          return {
            node,
            year: node.dataset.year,
            types: [...new Set(types.map(canonicalType))],
            text: normalize(
              node.textContent + " " + (node.dataset.extra || ""),
            ),
          };
        },
      );
      const add = (select, value, text) => {
        const option = document.createElement("option");
        option.value = value;
        option.textContent = text;
        select.appendChild(option);
      };
      [...new Set(papers.map((p) => p.year).filter(Boolean))]
        .sort()
        .reverse()
        .forEach((v) => add(year, v, v));
      // 每个区块独立管理动画；首次加载不播放，避免整页闪烁。
      const visibilityStates = new WeakMap();
      function setPaperVisible(node, visible) {
        const previous = visibilityStates.get(node);
        if (previous?.visible === visible) return;

        const reduced = window.matchMedia(
          "(prefers-reduced-motion: reduce)",
        ).matches;

        // 首次初始化或关闭动态效果时，直接切换。
        if (!previous || reduced || typeof node.animate !== "function") {
          previous?.animation?.cancel();
          visibilityStates.set(node, { visible, animation: null });
          node.hidden = !visible;
          node.inert = !visible;
          return;
        }

        // 在取消旧动画之前，记录当前实际尺寸，支持快速反向切换。
        function measure() {
          const style = getComputedStyle(node);

          return {
            height: `${node.getBoundingClientRect().height}px`,
            opacity: style.opacity,
            paddingTop: style.paddingTop,
            paddingBottom: style.paddingBottom,
            marginTop: style.marginTop,
            marginBottom: style.marginBottom,
            borderTopWidth: style.borderTopWidth,
            borderBottomWidth: style.borderBottomWidth,
          };
        }

        const collapsed = {
          height: "0px",
          opacity: "0",
          paddingTop: "0px",
          paddingBottom: "0px",
          marginTop: "0px",
          marginBottom: "0px",
          borderTopWidth: "0px",
          borderBottomWidth: "0px",
        };

        const from = node.hidden ? collapsed : measure();

        previous.animation?.cancel();

        // 恢复自然布局，测量完整高度。
        node.hidden = false;
        node.inert = !visible;

        const to = visible ? measure() : collapsed;
        const state = { visible, animation: null };
        visibilityStates.set(node, state);

        // 隔离 CSS transition，避免与高度动画互相干扰。
        const fixed = {
          boxSizing: "border-box",
          minHeight: "0px",
          overflow: "hidden",
          transition: "none",
        };

        const animation = node.animate(
          [
            { ...from, ...fixed },
            { ...to, ...fixed },
          ],
          {
            duration: 260,
            easing: "cubic-bezier(0.4, 0, 0.2, 1)",
            fill: "both",
          },
        );

        state.animation = animation;

        animation.onfinish = () => {
          // 忽略已经被新搜索结果替代的动画。
          if (visibilityStates.get(node) !== state) return;

          node.hidden = !visible;
          animation.cancel();
          state.animation = null;
        };
      }
      function update() {
        const words = normalize(query.value).split(" ").filter(Boolean);
        let count = 0;
        for (const paper of papers) {
          const match =
            (!year.value || paper.year === year.value) &&
            (!type.value || paper.types.includes(type.value)) &&
            words.every((w) => paper.text.includes(w));
          setPaperVisible(paper.node, match);
          if (match) count++;
        }
        root.querySelector("[data-count]").textContent = countTemplate
          .replaceAll("{count}", String(count))
          .replaceAll("{total}", String(papers.length));
        root.querySelector("[data-empty]").hidden = count !== 0;
      }
      query.addEventListener("input", update);
      year.addEventListener("change", update);
      type.addEventListener("change", update);
      root.querySelector("[data-reset]").addEventListener("click", () => {
        query.value = year.value = type.value = "";
        update();
        query.focus();
      });
      root.querySelector("[data-controls]").hidden = false;
      update();
    });
  }
  if (document.readyState === "loading")
    document.addEventListener("DOMContentLoaded", init, { once: true });
  else init();
})();
