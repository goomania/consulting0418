"""Generate all inner AISprint pages by assembling shared nav/footer with per-page body."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from build import build_page

OUT = Path(__file__).parent

# ============================================================================
# ABOUT PAGE
# ============================================================================
ABOUT_BODY = """
<section class="page-hero">
  <div class="container-wide">
    <div class="eyebrow mb-2" style="color: var(--accent);">About AISprint</div>
    <h1>A small practice,<br><em>built for long relationships.</em></h1>
    <p class="lead">
      AISprint was founded on a simple premise: most institutions do not need another vendor.
      They need a partner who will sit with the ambiguity, ask the uncomfortable questions, and
      leave the house in better order than they found it.
    </p>
  </div>
</section>

<div class="breadcrumb-row">
  <div class="container-wide">
    <a href="index.html">Home</a>
    <span class="sep">›</span>
    <span class="current">About</span>
  </div>
</div>

<section class="section">
  <div class="container split">
    <div class="split-sticky">
      <div class="eyebrow">Philosophy</div>
      <h2 class="h-display mt-2">What we<br>believe.</h2>
    </div>
    <div>
      <p class="lead mb-3">
        Good AI work is a long game of small, correct decisions. The models change, but the craft
        of fitting a technology to an institution does not.
      </p>
      <p class="mb-2">
        The firms that will matter in this decade are the ones who can translate between three
        languages at once — the language of language models, the language of enterprise data, and
        the language of the institutions those data describe. We work at that translation layer.
      </p>
      <p class="mb-2">
        We do not sell seats, licenses, or platforms. We sell judgment. Our deliverables are
        architectural decisions, working prototypes, and the written artifacts — proposals, memos,
        evaluation plans — that give institutions the confidence to move forward.
      </p>
      <p>
        When we finish an engagement, we expect you to be less dependent on us, not more.
      </p>
    </div>
  </div>
</section>

<section class="section bg-paper">
  <div class="container">
    <div class="eyebrow">Operating principles</div>
    <h2 class="h-display mt-2 mb-3">Six rules we follow,<br>in order of priority.</h2>

    <div class="principle">
      <div class="principle-num">No. 01</div>
      <div>
        <h4>Read before writing.</h4>
        <p>Every engagement begins with a documents-and-people inventory. We will not propose an architecture until we have read your SOPs, walked your data systems, and interviewed the people who will live with the result.</p>
      </div>
    </div>
    <div class="principle">
      <div class="principle-num">No. 02</div>
      <div>
        <h4>Name the trade-offs.</h4>
        <p>Latency vs. accuracy. On-prem vs. API. Build vs. buy. We do not hide these behind vendor jargon; we put them in a table, with your risk appetite on one axis and your budget on the other.</p>
      </div>
    </div>
    <div class="principle">
      <div class="principle-num">No. 03</div>
      <div>
        <h4>Architecture is a decision, not a preference.</h4>
        <p>RAG, MCP, fine-tuning, agents — each fits a specific shape of problem. We match the pattern to the institution, not the institution to our favorite pattern.</p>
      </div>
    </div>
    <div class="principle">
      <div class="principle-num">No. 04</div>
      <div>
        <h4>Ship something small and real.</h4>
        <p>Every engagement produces a working artifact within the first month. A demo, a prototype, a live search interface. Slides are insufficient evidence.</p>
      </div>
    </div>
    <div class="principle">
      <div class="principle-num">No. 05</div>
      <div>
        <h4>Write for the next person.</h4>
        <p>All documentation is written as if the reader is a thoughtful engineer who has never met us. This is the kindest thing we can do for your institution.</p>
      </div>
    </div>
    <div class="principle">
      <div class="principle-num">No. 06</div>
      <div>
        <h4>The engagement ends.</h4>
        <p>We design every project with a clear endpoint. If you want us to stay, it should be because we are solving new problems — not maintaining the last ones.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <div>
        <div class="eyebrow">Capabilities</div>
        <h2 class="h-display">Technical fluency.</h2>
      </div>
      <p class="lead">We are model-agnostic. We optimize for the specific task, data-sensitivity constraints, and infrastructure of each client.</p>
    </div>

    <div class="offer-grid">
      <div class="offer" data-reveal>
        <div class="kicker">Models</div>
        <h3>Language Models</h3>
        <p>Claude, GPT, Gemini, and open-weight models. We recommend based on the task, not the vendor relationship.</p>
      </div>
      <div class="offer" data-reveal>
        <div class="kicker">Retrieval</div>
        <h3>Retrieval Systems</h3>
        <p>Hybrid search, dense embeddings, reranking, and structured tool calls over SQL and REST APIs.</p>
      </div>
      <div class="offer" data-reveal>
        <div class="kicker">Integration</div>
        <h3>Integration Patterns</h3>
        <p>Model Context Protocol, agentic workflows, and the operational plumbing that makes models reliable.</p>
      </div>
      <div class="offer" data-reveal>
        <div class="kicker">Rigor</div>
        <h3>Evaluation</h3>
        <p>Rubric-based evals, faithfulness metrics, grant-ready evaluation frameworks for funders and accreditors.</p>
      </div>
    </div>
  </div>
</section>

<section class="section bg-paper">
  <div class="container split">
    <div class="split-sticky">
      <div class="eyebrow">Trajectory</div>
      <h2 class="h-display mt-2">Selected<br>milestones.</h2>
    </div>
    <div>
      <div class="principle">
        <div class="principle-num">2026</div>
        <div>
          <h4>Three concurrent university engagements</h4>
          <p>A leadership-program AI integration, a research-center RAG architecture, and a prospective institutional advancement extension — all scoped and active.</p>
        </div>
      </div>
      <div class="principle">
        <div class="principle-num">2026</div>
        <div>
          <h4>Workshops at an institutional AI expo</h4>
          <p>Led hands-on sessions on applied retrieval, enterprise MCP, and responsible AI evaluation — the catalyst for two follow-on engagements.</p>
        </div>
      </div>
      <div class="principle">
        <div class="principle-num">2025</div>
        <div>
          <h4>AISprint founded</h4>
          <p>Independent practice established to serve institutions — particularly those in higher education and mission-driven research — with the full AI strategy-to-implementation stack.</p>
        </div>
      </div>
      <div class="principle">
        <div class="principle-num">2024</div>
        <div>
          <h4>Early architecture work on enterprise AI patterns</h4>
          <p>Formative projects combining frontier language models with MCP server architectures over institutional data systems.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section-lg bg-dark">
  <div class="container text-center">
    <h2 class="h-display mb-2" style="color: var(--white); max-width: 20ch; margin-left:auto; margin-right:auto;">Curious whether we are the right fit?</h2>
    <a href="contact.html" class="btn btn-primary">Begin a conversation <span class="arr">→</span></a>
  </div>
</section>
"""

# ============================================================================
# SERVICES PAGE
# ============================================================================
SERVICES_BODY = """
<section class="page-hero">
  <div class="container-wide">
    <div class="eyebrow mb-2" style="color: var(--accent);">Services</div>
    <h1>Four practice areas.<br><em>One continuous arc.</em></h1>
    <p class="lead">
      Most engagements follow a recognizable shape: a readiness assessment, an architectural
      decision, a working prototype, and a plan for what comes next. Clients often begin in the middle.
    </p>
  </div>
</section>

<div class="breadcrumb-row">
  <div class="container-wide">
    <a href="index.html">Home</a>
    <span class="sep">›</span>
    <span class="current">Services</span>
  </div>
</div>

<section class="section" id="strategy">
  <div class="container split">
    <div class="split-sticky">
      <div class="eyebrow">Service No. 01</div>
      <h2 class="h-display mt-2">AI Strategy<br>&amp; Readiness.</h2>
    </div>
    <div>
      <p class="lead mb-3">For leadership teams who need to decide — with conviction — what to build, what to buy, and what to defer.</p>
      <p class="mb-2">Strategy engagements are short and intense. We spend two to four weeks reading your existing roadmaps, interviewing stakeholders across technical and business functions, and mapping your current capabilities against the opportunities your peers are pursuing.</p>
      <p class="mb-3">The deliverable is a written assessment you can circulate to your board, your funders, or your executive committee — not a slide deck, but a document that respects their time and reasoning.</p>

      <h4 class="h-md mb-2" style="font-family: var(--serif); font-weight: 500;">Typical deliverables</h4>
      <ul style="list-style: none; padding: 0; margin-bottom: 1.5rem;">
        <li style="padding: 0.75rem 0; border-top: 1px solid var(--border);"><strong style="color: var(--accent); margin-right: 0.75rem;">·</strong> Capability audit across people, data, and tooling</li>
        <li style="padding: 0.75rem 0; border-top: 1px solid var(--border);"><strong style="color: var(--accent); margin-right: 0.75rem;">·</strong> Prioritized opportunity map with cost and complexity estimates</li>
        <li style="padding: 0.75rem 0; border-top: 1px solid var(--border);"><strong style="color: var(--accent); margin-right: 0.75rem;">·</strong> Governance framework calibrated to your risk tolerance</li>
        <li style="padding: 0.75rem 0; border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);"><strong style="color: var(--accent); margin-right: 0.75rem;">·</strong> Investment roadmap with phase gates and decision criteria</li>
      </ul>
      <div class="tags">
        <span class="tag-pill">2–4 weeks</span>
        <span class="tag-pill">Executive audience</span>
        <span class="tag-pill">Written deliverable</span>
      </div>
    </div>
  </div>
</section>

<section class="section bg-paper" id="architecture">
  <div class="container split">
    <div class="split-sticky">
      <div class="eyebrow">Service No. 02</div>
      <h2 class="h-display mt-2">Architecture<br>&amp; Implementation.</h2>
    </div>
    <div>
      <p class="lead mb-3">Working software, not speculative diagrams. We design, build, and hand off production-grade AI systems.</p>
      <p class="mb-2">This is where most of our hours live. Clients bring us a specific system they want to stand up — a research knowledge base, a student-facing search tool, a staff-facing analytical assistant — and we ship it end-to-end.</p>
      <p class="mb-3">Our architectural preferences lean toward retrieval-augmented generation patterns with well-scoped tool calls via the Model Context Protocol. We work across cloud providers and are model-agnostic.</p>

      <h4 class="h-md mb-2" style="font-family: var(--serif); font-weight: 500;">Typical deliverables</h4>
      <ul style="list-style: none; padding: 0; margin-bottom: 1.5rem;">
        <li style="padding: 0.75rem 0; border-top: 1px solid var(--border);"><strong style="color: var(--accent); margin-right: 0.75rem;">·</strong> System architecture with data-flow and trust-boundary diagrams</li>
        <li style="padding: 0.75rem 0; border-top: 1px solid var(--border);"><strong style="color: var(--accent); margin-right: 0.75rem;">·</strong> Working prototype deployed in your environment</li>
        <li style="padding: 0.75rem 0; border-top: 1px solid var(--border);"><strong style="color: var(--accent); margin-right: 0.75rem;">·</strong> MCP servers, retrieval pipelines, and evaluation harnesses</li>
        <li style="padding: 0.75rem 0; border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);"><strong style="color: var(--accent); margin-right: 0.75rem;">·</strong> Engineering handoff documentation for your team</li>
      </ul>
      <div class="tags">
        <span class="tag-pill">6–16 weeks</span>
        <span class="tag-pill">Technical deliverable</span>
        <span class="tag-pill">Production-grade</span>
      </div>
    </div>
  </div>
</section>

<section class="section" id="program">
  <div class="container split">
    <div class="split-sticky">
      <div class="eyebrow">Service No. 03</div>
      <h2 class="h-display mt-2">Program Design<br>&amp; Integration.</h2>
    </div>
    <div>
      <p class="lead mb-3">For academic programs, fellowships, and training cohorts integrating AI into curriculum and pedagogy.</p>
      <p class="mb-2">Software is the easy part. Getting faculty, staff, and students to adopt a new tool — without triggering the immune response institutions reserve for change — is the actual work.</p>
      <p class="mb-3">Our program-design engagements combine instructional co-design with a clear-eyed change plan: syllabus inserts, facilitator guides, faculty onboarding sessions, and student-facing communications tuned to the culture of your program.</p>

      <h4 class="h-md mb-2" style="font-family: var(--serif); font-weight: 500;">Typical deliverables</h4>
      <ul style="list-style: none; padding: 0; margin-bottom: 1.5rem;">
        <li style="padding: 0.75rem 0; border-top: 1px solid var(--border);"><strong style="color: var(--accent); margin-right: 0.75rem;">·</strong> Curricular integration map with touchpoints and artifacts</li>
        <li style="padding: 0.75rem 0; border-top: 1px solid var(--border);"><strong style="color: var(--accent); margin-right: 0.75rem;">·</strong> Faculty and staff training sessions with materials</li>
        <li style="padding: 0.75rem 0; border-top: 1px solid var(--border);"><strong style="color: var(--accent); margin-right: 0.75rem;">·</strong> Student-facing prompt libraries and guardrails</li>
        <li style="padding: 0.75rem 0; border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);"><strong style="color: var(--accent); margin-right: 0.75rem;">·</strong> Adoption metrics and a semester-long evaluation plan</li>
      </ul>
      <div class="tags">
        <span class="tag-pill">One semester</span>
        <span class="tag-pill">Instructional co-design</span>
        <span class="tag-pill">Change management</span>
      </div>
    </div>
  </div>
</section>

<section class="section bg-paper" id="research">
  <div class="container split">
    <div class="split-sticky">
      <div class="eyebrow">Service No. 04</div>
      <h2 class="h-display mt-2">Applied<br>Research.</h2>
    </div>
    <div>
      <p class="lead mb-3">Co-authored publications, grant-ready technical appendices, and the evaluation frameworks funders now expect.</p>
      <p class="mb-2">Research centers and grant-funded programs increasingly need to demonstrate that their AI work is rigorous, reproducible, and impactful. We bring the methodological chops and the writing discipline required to meet that bar.</p>
      <p class="mb-3">We have co-authored technical sections of multi-million-dollar renewal proposals, designed evaluation frameworks for federal funders, and partnered with faculty on peer-reviewed publications.</p>

      <h4 class="h-md mb-2" style="font-family: var(--serif); font-weight: 500;">Typical deliverables</h4>
      <ul style="list-style: none; padding: 0; margin-bottom: 1.5rem;">
        <li style="padding: 0.75rem 0; border-top: 1px solid var(--border);"><strong style="color: var(--accent); margin-right: 0.75rem;">·</strong> Grant technical appendices and methodology sections</li>
        <li style="padding: 0.75rem 0; border-top: 1px solid var(--border);"><strong style="color: var(--accent); margin-right: 0.75rem;">·</strong> Co-authored conference and journal submissions</li>
        <li style="padding: 0.75rem 0; border-top: 1px solid var(--border);"><strong style="color: var(--accent); margin-right: 0.75rem;">·</strong> Evaluation frameworks for funders and accreditors</li>
        <li style="padding: 0.75rem 0; border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);"><strong style="color: var(--accent); margin-right: 0.75rem;">·</strong> Reproducible benchmarks and datasets</li>
      </ul>
      <div class="tags">
        <span class="tag-pill">Rolling</span>
        <span class="tag-pill">Co-authorship</span>
        <span class="tag-pill">Peer-review ready</span>
      </div>
    </div>
  </div>
</section>

<section class="section-lg bg-dark">
  <div class="container text-center">
    <h2 class="h-display mb-2" style="color: var(--white); max-width: 22ch; margin-left:auto; margin-right:auto;">Ready to scope something real?</h2>
    <p class="lead mb-3" style="color: #c3ccd6; margin-left:auto; margin-right:auto;">We offer a complimentary 45-minute scoping call. Bring a problem, not a spec.</p>
    <a href="contact.html" class="btn btn-primary">Schedule a call <span class="arr">→</span></a>
  </div>
</section>
"""

# ============================================================================
# HOW WE HELP PAGE (engagement process, phases)
# ============================================================================
HOW_BODY = """
<section class="page-hero">
  <div class="container-wide">
    <div class="eyebrow mb-2" style="color: var(--accent);">How we help clients</div>
    <h1>From the first question<br><em>to the working system.</em></h1>
    <p class="lead">
      Every AISprint engagement unfolds through four phases. Each phase has a clear input, a
      clear output, and an exit criterion. You know what you're getting before we begin.
    </p>
  </div>
</section>

<div class="breadcrumb-row">
  <div class="container-wide">
    <a href="index.html">Home</a>
    <span class="sep">›</span>
    <span class="current">How we help</span>
  </div>
</div>

<section class="section">
  <div class="container">
    <div class="feature-row">
      <div>
        <div class="eyebrow">Phase i</div>
        <h2 class="h-xl mt-2 mb-2">Discovery.</h2>
        <p class="lead mb-2">One to two weeks of document review, systems walkthroughs, and stakeholder interviews. No architecture decisions yet.</p>
        <p class="mb-2">We read everything you send us — SOPs, past proposals, data dictionaries, org charts. We sit in on your existing workflows. We interview the people who will actually use what we build, not just the people sponsoring the engagement.</p>
        <p>We leave this phase with a written discovery memo: what we heard, what we saw, and the three to five most promising intervention points we've identified.</p>
      </div>
      <div class="feature-img"><object data="assets/graphic-flow.svg" type="image/svg+xml" aria-label=""></object></div>
    </div>

    <div class="feature-row reverse">
      <div class="feature-img"><object data="assets/graphic-grid.svg" type="image/svg+xml" aria-label=""></object></div>
      <div>
        <div class="eyebrow">Phase ii</div>
        <h2 class="h-xl mt-2 mb-2">Proposal.</h2>
        <p class="lead mb-2">A written scope with architectural decisions, trade-offs named, milestones dated, and exit criteria defined.</p>
        <p class="mb-2">We don't do SOWs that hide the trade-offs. Our proposals lay out the architectural options — RAG vs. agents, on-prem vs. API, build vs. buy — and show the reasoning behind our recommendation.</p>
        <p>You can take our proposal to your CFO, your CIO, or your board. It is written to be read by non-technical decision-makers without losing the technical fidelity your engineers need.</p>
      </div>
    </div>

    <div class="feature-row">
      <div>
        <div class="eyebrow">Phase iii</div>
        <h2 class="h-xl mt-2 mb-2">Build.</h2>
        <p class="lead mb-2">We ship a working artifact within thirty days and iterate weekly, with plain-language status notes to every stakeholder.</p>
        <p class="mb-2">Week-one deliverable, week-four working prototype. That cadence is non-negotiable. We'd rather ship something small and real than something large and speculative.</p>
        <p>Every Friday, you get a short written update: what we built, what we learned, and what's coming next week. No slide decks, no status theater.</p>
      </div>
      <div class="feature-img"><object data="assets/graphic-particles.svg" type="image/svg+xml" aria-label=""></object></div>
    </div>

    <div class="feature-row reverse">
      <div class="feature-img"><object data="assets/graphic-orbits.svg" type="image/svg+xml" aria-label=""></object></div>
      <div>
        <div class="eyebrow">Phase iv</div>
        <h2 class="h-xl mt-2 mb-2">Handoff.</h2>
        <p class="lead mb-2">Documentation, a live walkthrough with your engineers, and a short written postmortem. You own what we built.</p>
        <p class="mb-2">Engineering handoff is an explicit phase, not an afterthought. We write documentation for the next engineer — not for us to read again. We run a live walkthrough with your technical team and answer questions until they're answered.</p>
        <p>And we write a short postmortem: what went well, what didn't, and what we'd do differently if we started over. That document is yours.</p>
      </div>
    </div>
  </div>
</section>

<section class="section bg-paper">
  <div class="container">
    <div class="section-head">
      <div>
        <div class="eyebrow">Who we help</div>
        <h2 class="h-display">Institutions we serve.</h2>
      </div>
      <p class="lead">
        We work with organizations that treat the AI decision seriously — and want a partner who treats it the same way.
      </p>
    </div>

    <div class="cap-grid">
      <article class="cap-card" data-reveal>
        <div class="thumb"><object data="assets/graphic-flow.svg" type="image/svg+xml" aria-label=""></object></div>
        <div class="body">
          <h3>Higher Education</h3>
          <p>Schools, colleges, and academic programs integrating AI into curriculum, operations, and student-facing services.</p>
        </div>
      </article>
      <article class="cap-card" data-reveal>
        <div class="thumb"><object data="assets/graphic-rings.svg" type="image/svg+xml" aria-label=""></object></div>
        <div class="body">
          <h3>Research Centers</h3>
          <p>University research centers and institutes building knowledge bases, retrieval interfaces, and funder-ready evaluation frameworks.</p>
        </div>
      </article>
      <article class="cap-card" data-reveal>
        <div class="thumb"><object data="assets/graphic-grid.svg" type="image/svg+xml" aria-label=""></object></div>
        <div class="body">
          <h3>Institutional Advancement</h3>
          <p>Development and fundraising teams extending enterprise AI into CRM estates — Blackbaud CRM and Raiser's Edge NXT patterns.</p>
        </div>
      </article>
      <article class="cap-card" data-reveal>
        <div class="thumb"><object data="assets/graphic-mesh.svg" type="image/svg+xml" aria-label=""></object></div>
        <div class="body">
          <h3>Mission-Driven Nonprofits</h3>
          <p>Advocacy organizations, foundations, and policy programs applying AI responsibly to communications and research functions.</p>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="quote-section">
  <div class="container">
    <p class="quote-text" data-reveal>
      The recommendation of where <em>not</em> to use AI was the most valuable part of the engagement.
      That's not something you get from most consultants.
    </p>
    <div class="quote-attr">— Program Director · 2026</div>
  </div>
</section>

<section class="section-lg bg-dark">
  <div class="container text-center">
    <h2 class="h-display mb-2" style="color: var(--white); max-width: 22ch; margin-left:auto; margin-right:auto;">Start where it fits. We can meet you anywhere in the arc.</h2>
    <a href="contact.html" class="btn btn-primary">Begin a conversation <span class="arr">→</span></a>
  </div>
</section>
"""

# ============================================================================
# CASE STUDIES PAGE
# ============================================================================
CASES_BODY = """
<section class="page-hero">
  <div class="container-wide">
    <div class="eyebrow mb-2" style="color: var(--accent);">Selected work</div>
    <h1>What we've built,<br><em>and why it mattered.</em></h1>
    <p class="lead">
      A selection of engagements that illustrate how we work. Names and identifying details are
      generalized at clients' request; the architectural patterns and outcomes are faithful to
      the real projects.
    </p>
  </div>
</section>

<div class="breadcrumb-row">
  <div class="container-wide">
    <a href="index.html">Home</a>
    <span class="sep">›</span>
    <span class="current">Case studies</span>
  </div>
</div>

<section class="section">
  <div class="container">
    <div class="eyebrow mb-2">Featured engagement</div>
    <h2 class="h-display mb-3">AI integration for a public-service leadership program.</h2>

    <article class="impact-featured" data-reveal>
      <div class="thumb"><object data="assets/graphic-flow.svg" type="image/svg+xml" aria-label=""></object></div>
      <div class="body">
        <div class="tag-pill" style="margin-bottom: 1rem; display: inline-block;">Higher Education · 2026</div>
        <h3>A three-touchpoint curricular integration — and two deliberate abstentions.</h3>
        <p class="mb-2">A cohort-based leadership program serving veterans transitioning to public office wanted to integrate AI tools into its curriculum without losing the program's pedagogical identity. The program director had watched peer institutions bolt on "AI modules" that felt like technology demos, and she wanted something different.</p>
        <p class="mb-3">We spent two weeks in discovery — reviewing syllabi, interviewing the director and instructional designer, and working with the MPA student team already embedded in the program. We proposed three touchpoints where AI genuinely amplified existing learning objectives, plus one optional deep-dive module. For each touchpoint, we drafted the facilitator guide, prompt library, and student-facing framing. We also recommended <em>against</em> two touchpoints the program had considered — the cost-to-benefit was unfavorable, and we said so in writing.</p>
        <a href="contact.html" class="btn-link">Discuss a similar engagement <span>→</span></a>
      </div>
    </article>
  </div>
</section>

<section class="section bg-paper">
  <div class="container">
    <div class="eyebrow mb-2">Additional engagements</div>
    <h2 class="h-display mb-3">Recent work.</h2>

    <div class="impact-grid">
      <article class="impact-card" data-reveal>
        <div class="thumb"><object data="assets/graphic-grid.svg" type="image/svg+xml" aria-label=""></object></div>
        <div class="tag">Research · 2026</div>
        <h3>RAG architecture for a social justice research center</h3>
        <div class="meta">8-week engagement</div>
        <p>Designed a retrieval pipeline over the center's Power BI data portal and qualitative research archive, integrated with a natural-language interface for fellows and grant auditors. Pattern is now informing a multi-year renewal proposal to a major private foundation.</p>
      </article>
      <article class="impact-card" data-reveal>
        <div class="thumb"><object data="assets/graphic-rings.svg" type="image/svg+xml" aria-label=""></object></div>
        <div class="tag">Enterprise AI · 2026</div>
        <h3>Extending AI into institutional advancement</h3>
        <div class="meta">Discovery + proposal</div>
        <p>Proposed an extension of an existing Claude + MCP architecture from academic course search into the CRM advancement data estate. Included a framework for Blackbaud CRM vs. Raiser's Edge NXT integration patterns, with phased rollout and risk framing for the CDO's office.</p>
      </article>
      <article class="impact-card" data-reveal>
        <div class="thumb"><object data="assets/graphic-particles.svg" type="image/svg+xml" aria-label=""></object></div>
        <div class="tag">Workshop · 2026</div>
        <h3>Applied AI workshops for a research expo</h3>
        <div class="meta">Multi-session engagement</div>
        <p>Designed and delivered a hands-on workshop series for faculty and staff across a major research university, covering applied retrieval, responsible evaluation, and enterprise MCP patterns. The workshops directly catalyzed two follow-on consulting engagements.</p>
      </article>
      <article class="impact-card" data-reveal>
        <div class="thumb"><object data="assets/graphic-mesh.svg" type="image/svg+xml" aria-label=""></object></div>
        <div class="tag">Nonprofit · 2025</div>
        <h3>AI readiness audit for a mid-sized nonprofit</h3>
        <div class="meta">3-week engagement</div>
        <p>Three-week capability and governance assessment for an advocacy organization preparing to deploy AI tools across its communications and research functions. Delivered a prioritized roadmap, lightweight governance framework, and six-month investment plan.</p>
      </article>
      <article class="impact-card" data-reveal>
        <div class="thumb"><object data="assets/graphic-orbits.svg" type="image/svg+xml" aria-label=""></object></div>
        <div class="tag">Higher Education · 2025</div>
        <h3>Course discovery tool architecture review</h3>
        <div class="meta">Advisory engagement</div>
        <p>Technical architecture review of a university's student-facing course search tool built on Claude and MCP. Delivered recommendations on latency optimization, retrieval quality, and the sequence of MCP round-trips slowing production response times.</p>
      </article>
      <article class="impact-card" data-reveal>
        <div class="thumb"><object data="assets/graphic-flow.svg" type="image/svg+xml" aria-label=""></object></div>
        <div class="tag">Research · 2025</div>
        <h3>Evaluation framework for a federally-funded AI study</h3>
        <div class="meta">Methodology support</div>
        <p>Authored the methodology and evaluation framework section of a federal grant renewal application, including reproducible benchmarks and a faithfulness-metrics plan tailored to the funder's reporting requirements.</p>
      </article>
    </div>
  </div>
</section>

<section class="stats-band">
  <div class="stat">
    <div class="stat-value"><em>30</em> days</div>
    <div class="stat-label">To working prototype</div>
  </div>
  <div class="stat">
    <div class="stat-value"><em>2</em>×</div>
    <div class="stat-label">Avg. scope expansion</div>
  </div>
  <div class="stat">
    <div class="stat-value">$<em>4.2</em>M</div>
    <div class="stat-label">Grant funding informed</div>
  </div>
  <div class="stat">
    <div class="stat-value"><em>100</em>%</div>
    <div class="stat-label">On-time handoff</div>
  </div>
</section>

<section class="section-lg bg-dark">
  <div class="container text-center">
    <h2 class="h-display mb-2" style="color: var(--white); max-width: 22ch; margin-left:auto; margin-right:auto;">Could yours be the next engagement?</h2>
    <a href="contact.html" class="btn btn-primary">Start a conversation <span class="arr">→</span></a>
  </div>
</section>
"""

# ============================================================================
# INSIGHTS PAGE
# ============================================================================
INSIGHTS_BODY = """
<section class="page-hero">
  <div class="container-wide">
    <div class="eyebrow mb-2" style="color: var(--accent);">Our insights</div>
    <h1>Thinking in public<br><em>about applied AI.</em></h1>
    <p class="lead">
      Articles, white papers, and case notes from our engagements. Written for practitioners
      and decision-makers who want depth, not hype.
    </p>
  </div>
</section>

<div class="breadcrumb-row">
  <div class="container-wide">
    <a href="index.html">Home</a>
    <span class="sep">›</span>
    <span class="current">Insights</span>
  </div>
</div>

<section class="section">
  <div class="container">
    <div class="eyebrow mb-2">Featured</div>
    <h2 class="h-display mb-3">Latest thinking.</h2>

    <article class="impact-featured" data-reveal>
      <div class="thumb"><object data="assets/graphic-mesh.svg" type="image/svg+xml" aria-label=""></object></div>
      <div class="body">
        <div class="tag-pill" style="margin-bottom: 1rem; display: inline-block;">Article · March 2026</div>
        <h3>Evaluating RAG systems in regulated institutional contexts</h3>
        <p class="mb-2">Most RAG evaluation frameworks were designed for public-facing consumer applications. Universities, research centers, and regulated institutions need a different set of metrics — ones that account for provenance, auditability, and faithfulness to cited sources. This article walks through the framework we've refined across four recent engagements.</p>
        <a href="#" class="btn-link">Read the article <span>→</span></a>
      </div>
    </article>
  </div>
</section>

<section class="section bg-paper">
  <div class="container">
    <div class="eyebrow mb-2">All insights</div>
    <h2 class="h-display mb-3">Recent publications.</h2>

    <div class="insights-grid">
      <a href="#" class="insight-card" data-reveal>
        <div class="thumb"><object data="assets/graphic-orbits.svg" type="image/svg+xml" aria-label=""></object></div>
        <div class="kind">White Paper</div>
        <h3>The MCP pattern for university data estates</h3>
        <div class="date">February 2026</div>
      </a>
      <a href="#" class="insight-card" data-reveal>
        <div class="thumb"><object data="assets/graphic-particles.svg" type="image/svg+xml" aria-label=""></object></div>
        <div class="kind">Article</div>
        <h3>When not to use AI: a curricular integration framework</h3>
        <div class="date">January 2026</div>
      </a>
      <a href="#" class="insight-card" data-reveal>
        <div class="thumb"><object data="assets/graphic-grid.svg" type="image/svg+xml" aria-label=""></object></div>
        <div class="kind">Case Note</div>
        <h3>Architecting advancement AI: CRM, MCP, and the fundraising stack</h3>
        <div class="date">December 2025</div>
      </a>
      <a href="#" class="insight-card" data-reveal>
        <div class="thumb"><object data="assets/graphic-flow.svg" type="image/svg+xml" aria-label=""></object></div>
        <div class="kind">Article</div>
        <h3>Retrieval over Power BI: a pragmatic pattern</h3>
        <div class="date">November 2025</div>
      </a>
      <a href="#" class="insight-card" data-reveal>
        <div class="thumb"><object data="assets/graphic-rings.svg" type="image/svg+xml" aria-label=""></object></div>
        <div class="kind">White Paper</div>
        <h3>Structured tool calls over parameterized SQL: why Claude doesn't write SQL directly</h3>
        <div class="date">October 2025</div>
      </a>
      <a href="#" class="insight-card" data-reveal>
        <div class="thumb"><object data="assets/graphic-mesh.svg" type="image/svg+xml" aria-label=""></object></div>
        <div class="kind">Article</div>
        <h3>Latency in production RAG: three sources and what to do about them</h3>
        <div class="date">September 2025</div>
      </a>
      <a href="#" class="insight-card" data-reveal>
        <div class="thumb"><object data="assets/graphic-particles.svg" type="image/svg+xml" aria-label=""></object></div>
        <div class="kind">Case Note</div>
        <h3>How a 20-hour engagement became a three-program rollout</h3>
        <div class="date">August 2025</div>
      </a>
      <a href="#" class="insight-card" data-reveal>
        <div class="thumb"><object data="assets/graphic-orbits.svg" type="image/svg+xml" aria-label=""></object></div>
        <div class="kind">Article</div>
        <h3>Grant-ready evaluation frameworks: what funders actually want</h3>
        <div class="date">July 2025</div>
      </a>
    </div>
  </div>
</section>

<section class="section-lg bg-dark">
  <div class="container text-center">
    <div class="eyebrow mb-2">Subscribe</div>
    <h2 class="h-display mb-2" style="color: var(--white); max-width: 22ch; margin-left:auto; margin-right:auto;">A quarterly note, no more.</h2>
    <p class="lead mb-3" style="color: #c3ccd6; margin-left:auto; margin-right:auto;">We publish our longest-form thinking four times a year. Drop your email and we'll send it when it's ready.</p>
    <a href="contact.html" class="btn btn-primary">Get the next issue <span class="arr">→</span></a>
  </div>
</section>
"""

# ============================================================================
# CONTACT PAGE
# ============================================================================
CONTACT_BODY = """
<section class="page-hero">
  <div class="container-wide">
    <div class="eyebrow mb-2" style="color: var(--accent);">Contact</div>
    <h1>Write to us.<br><em>We read every inquiry.</em></h1>
    <p class="lead">
      We take on a small number of engagements each quarter and prefer starting with a real
      conversation rather than a generic scoping form. Tell us what you are trying to do, what
      has made it hard, and what a good outcome would look like.
    </p>
  </div>
</section>

<div class="breadcrumb-row">
  <div class="container-wide">
    <a href="index.html">Home</a>
    <span class="sep">›</span>
    <span class="current">Contact</span>
  </div>
</div>

<section class="section">
  <div class="container split">
    <div class="split-sticky">
      <div class="eyebrow">Inquiries</div>
      <h2 class="h-display mt-2 mb-2">Begin a<br>conversation.</h2>
      <p class="mt-2">All fields are optional except those marked required. We respond within two business days. If we're not the right fit, we'll say so and point you to someone who is.</p>
    </div>

    <div>
      <form class="form-grid" data-demo-form novalidate>
        <div class="field">
          <label for="name">Name *</label>
          <input type="text" id="name" name="name" required>
        </div>
        <div class="field">
          <label for="org">Organization</label>
          <input type="text" id="org" name="org">
        </div>
        <div class="field">
          <label for="email">Email *</label>
          <input type="email" id="email" name="email" required>
        </div>
        <div class="field">
          <label for="role">Role</label>
          <input type="text" id="role" name="role">
        </div>
        <div class="field full">
          <label for="service">What are you exploring?</label>
          <select id="service" name="service">
            <option>AI strategy &amp; readiness</option>
            <option>Architecture &amp; implementation</option>
            <option>Program design &amp; integration</option>
            <option>Applied research &amp; publications</option>
            <option>Not yet sure — let's talk</option>
          </select>
        </div>
        <div class="field full">
          <label for="message">Tell us about it *</label>
          <textarea id="message" name="message" placeholder="What are you trying to accomplish? What has made it hard? What does a good outcome look like?" required></textarea>
        </div>
        <div class="field full">
          <label for="timeline">When would you like to start?</label>
          <select id="timeline" name="timeline">
            <option>This quarter</option>
            <option>Next quarter</option>
            <option>Within the year</option>
            <option>Exploratory — no timeline yet</option>
          </select>
        </div>
        <div class="full" style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem; margin-top:1rem;">
          <span style="font-size:0.85rem; color:var(--muted);">We respond within two business days.</span>
          <button type="submit" class="btn btn-primary">Send inquiry <span class="arr">→</span></button>
        </div>
        <div class="form-msg full" style="display:none; grid-column: 1 / -1;">
          Thank you — your note has been received. We will write back within two business days.
        </div>
      </form>
    </div>
  </div>
</section>

<section class="section bg-paper">
  <div class="container">
    <div class="eyebrow mb-2">Other ways to reach us</div>
    <h2 class="h-display mb-3">Or, more directly.</h2>

    <div class="offer-grid">
      <div class="offer">
        <div class="kicker">By email</div>
        <h3>hello@aisprint.ai</h3>
        <p>For new engagements, partnership inquiries, and press.</p>
      </div>
      <div class="offer">
        <div class="kicker">A short call</div>
        <h3>45 minutes</h3>
        <p>Complimentary scoping call. Bring a problem; a spec is not required.</p>
      </div>
      <div class="offer">
        <div class="kicker">In person</div>
        <h3>Syracuse, NY</h3>
        <p>Based in Syracuse. We travel regularly throughout the Northeast corridor.</p>
      </div>
      <div class="offer">
        <div class="kicker">Follow</div>
        <h3>LinkedIn · Medium</h3>
        <p>Our writing cross-posts to Medium. Follow there for the full feed.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="eyebrow mb-2">Frequently asked</div>
    <h2 class="h-display mb-3">A few questions<br>we anticipate.</h2>

    <div style="max-width: 900px;">
      <details class="faq">
        <summary>What does a typical engagement cost?</summary>
        <p>Strategy engagements typically range from $18–40K. Architecture and implementation projects generally run $60–180K depending on scope and integration complexity. We scope every engagement in writing before work begins; we never bill beyond the scope without your written approval.</p>
      </details>
      <details class="faq">
        <summary>Do you work outside higher education?</summary>
        <p>Yes. While universities are a significant share of our portfolio, we also work with research institutes, nonprofits, and mission-driven enterprises. What we look for is an institution with a real problem, a willingness to engage substantively, and a culture that takes the work seriously.</p>
      </details>
      <details class="faq">
        <summary>Are you model-agnostic?</summary>
        <p>Yes. We are not resellers and do not receive vendor commissions. We recommend the model — proprietary or open-weight — best fit to the task, the data-sensitivity constraints, and the client's infrastructure.</p>
      </details>
      <details class="faq">
        <summary>Can you work alongside our existing vendors?</summary>
        <p>Often, yes. Many of our engagements involve stitching our work into an existing stack — enterprise search, CRM, data warehouse, LMS. We are comfortable in that role and will happily coordinate with your incumbent partners.</p>
      </details>
      <details class="faq">
        <summary>How quickly can you start?</summary>
        <p>For discovery and strategy work, typically within two to three weeks of a signed SOW. Implementation work depends on scope and on our current engagement load; we'll tell you honestly when we can begin.</p>
      </details>
      <details class="faq">
        <summary>Do you offer ongoing support after handoff?</summary>
        <p>We offer optional 90-day advisory retainers after major implementations — a few hours per month for questions, tuning, and follow-up. We do not offer open-ended maintenance contracts; your team should own what we build.</p>
      </details>
    </div>
  </div>
</section>
"""

# ============================================================================
# WRITE ALL PAGES
# ============================================================================
PAGES = [
    ("about.html",        "About — AISprint",                             "AISprint is a boutique AI consulting practice. A small team built for long client relationships.",           ABOUT_BODY,     "about"),
    ("services.html",     "Services — AISprint",                          "Four AI consulting service lines: strategy, architecture, program design, applied research.",                   SERVICES_BODY,  "services"),
    ("how-we-help.html",  "How we help — AISprint",                       "A four-phase AI consulting engagement model: discovery, proposal, build, handoff.",                              HOW_BODY,       "how-we-help"),
    ("case-studies.html", "Case studies — AISprint",                      "Selected AISprint engagements in higher education, research, and institutional advancement.",                   CASES_BODY,     "case-studies"),
    ("insights.html",     "Insights — AISprint",                          "AISprint articles, white papers, and case notes on applied AI for institutions.",                                INSIGHTS_BODY,  "insights"),
    ("contact.html",      "Contact — AISprint",                           "Begin a conversation with AISprint. We respond within two business days.",                                       CONTACT_BODY,   "contact"),
]

for filename, title, description, body, nav_slug in PAGES:
    html = build_page(filename, title, description, body, nav_slug)
    (OUT / filename).write_text(html, encoding="utf-8")
    print(f"wrote {filename} ({len(html):,} chars)")

print("\nAll pages generated.")
