"""Evaluation scenarios for the five acceptance criteria."""

# The project author supplied these ten self-authored texts for criterion 1.
USER_WRITING = [
    """Setting up a dual-monitor workstation requires more attention to ergonomics than most people realize. Begin by placing your primary monitor directly in front of you, roughly an arm's length away, with the top third of the screen sitting at eye level to prevent neck strain. Position the secondary monitor immediately adjacent to the first, angled slightly inward to reduce excessive head turning. Route display cables, power cords, and peripheral connections through designated cable channels or zip ties along the monitor arms before securing them to the desk frame. Once the hardware is physically aligned, access your operating system’s display settings to configure the layout so the digital cursor passes smoothly across both screens at the exact matching height.""",
    """A quiet Sunday afternoon provides the ideal atmosphere to reorganize a personal digital workspace. Sifting through months of accumulated desktop icons, unfiled downloads, and half-finished drafts can initially feel tedious, but establishing a structured hierarchy quickly brings clarity. Grouping documents into active projects, reference materials, and long-term archives clears visual clutter and immediately streamlines daily navigation. Emptying the trash bin and watching the storage meter rebound offers a subtle, refreshing sense of accomplishment. By late afternoon, a tidy directory tree and a clean desktop leave behind a calm, ready-to-work canvas for the week ahead.""",
    """Arrival stands out as one of the most compelling science fiction films of the past decade because it grounds extraordinary cosmic events in intimate human emotion. Rather than leaning on typical explosive confrontations or catastrophic spectacle, the narrative centers on linguistics, patience, and the intricate puzzle of communication. Amy Adams delivers a remarkably subtle, grounded performance as Dr. Louise Banks, conveying profound intellectual curiosity alongside a quiet, simmering grief. The visual aesthetic—dominated by muted palettes, brutalist architecture, and atmospheric mist—reinforces the unsettling yet awe-inspiring tone. Combined with Jóhann Jóhannsson’s haunting score, the film elevates a classic alien encounter into a moving meditation on time, connection, and memory.""",
    """Taking a brisk walk through the neighborhood during the transition between late autumn and early winter reveals subtle shifts in the landscape. The deciduous trees, stripped bare of their foliage, expose intricate branch structures against a pale gray sky, while sharp gusts of wind scatter dry leaves across empty sidewalks. Frost often lingers along the edges of shaded lawns well past noon, giving the ground a faint, crystalline sheen. Neighborhood chimneys begin sending faint wisps of woodsmoke into the cool air, blending with the smell of damp soil and drying pine needles. It is a quiet, contemplative time of day that offers a distinct sense of stillness.""",
    """Making a reliable pour-over coffee comes down to thermal control and steady pacing. Begin by bringing filtered water to roughly 200°F (93°C) and weighing out twenty grams of medium-coarse coffee grounds. Place a paper filter into the dripper and rinse it thoroughly with hot water to eliminate paper residue and preheat the decanter, discarding the rinse water afterward. Add the ground coffee, level the bed, and tare your digital scale. Start a timer and gently pour sixty grams of water in concentric circles from the center outward, allowing the coffee to bloom for forty-five seconds. Slowly add the remaining water in steady, measured intervals until you hit three hundred grams, keeping the water level consistent.""",
    """The debate between physical books and e-readers often reduces to a false choice between tactile nostalgia and raw utility. Digital readers undoubtedly excel at convenience: storing hundreds of unabridged volumes inside an ultralight frame with an adjustable, front-lit screen makes traveling seamless. Yet printed books provide distinct spatial landmarks—the shifting physical weight between your left and right hands, the texture of particular paper stocks, and the ease of flipping back and forth between maps, appendices, and chapters. While an e-reader is arguably the superior tool for high-volume consumption, physical editions anchor the reading experience to a specific time, place, and sensory memory that pure digital formats rarely match.""",
    """Early morning light rail commutes carry a distinctive, rhythmic ambiance that borders on communal silence. Passengers sit huddled in heavy coats, insulated inside personal headphones or engrossed in books, trading unspoken acknowledgments as the doors slide shut at every platform. The gentle hum of the electric motor accelerates into a steady drone, punctuated only by automated arrival announcements and the occasional click of a transit pass against the fare reader. As the train clears suburban stops and approaches the urban core, morning sunlight cuts across the windows, casting long shadows across the aisle. It is a predictable, shared routine that marks the start of the day.""",
    """Visiting a neighborhood diner early on a weekday morning is a lesson in unpretentious efficiency. The menu rarely changes, offering straightforward plates of golden hash browns crisped to order on a seasoned flattop grill, eggs cooked to your preference, and thick-cut sourdough toast. The waitstaff works with practiced speed, keeping heavy ceramic mugs constantly topped off with hot, bold drip coffee without ever needing to ask. The low murmur of local conversations mixes comfortably with the clatter of silverware and the steady sizzle behind the counter, creating a dependable, welcoming space where breakfast remains simple, satisfying, and refreshingly devoid of modern culinary fuss.""",
    """Learning to care for a collection of houseplants is essentially an exercise in restrained observation rather than constant intervention. Most newcomers overwater their plants out of goodwill, inadvertently suffocating roots that require oxygen just as much as moisture. The most effective approach involves checking the soil moisture several inches down with a finger or moisture meter, adjusting the position relative to ambient window light, and allowing the plant to acclimate without frequent relocation. Over time, subtle signs—a slight loss of leaf turgor, a pale discoloration, or new shoots emerging along the stem—become clear, intuitive indicators of what the plant actually needs to thrive.""",
    """Keeping a dedicated, written notebook for active projects remains far more effective for deep work than relying entirely on digital task managers. While project management software excels at team collaboration, assigning deadlines, and automated reporting, physical notebooks eliminate the constant lure of browser notifications and app switching. Jotting down rough logic, diagramming system workflows, or manually checking off milestones engages cognitive processing in a deliberate, tactile way. The open notebook resting beside the keyboard acts as a steady anchor for your attention, serving as an accessible scratchpad for fleeting ideas that would otherwise get lost in digital disorganization.""",
]

# These fixtures are explicitly AI-generated control samples for criterion 5.
AI_CONTROL = [
    """Artificial intelligence can support modern organizations by automating routine analysis and producing consistent summaries. A responsible deployment begins with a clear goal, a documented data source, and human review for consequential decisions. Teams should measure accuracy, monitor error patterns, and provide a simple path for people to challenge an outcome. When these safeguards are present, automation can reduce repetitive work while preserving accountability and trust.""",
    """Effective project planning follows a predictable sequence. First, define the desired outcome and identify the people affected by it. Next, divide the work into manageable tasks, assign owners, and establish realistic dates. Review progress regularly, communicate changes early, and record decisions so the team can learn from each milestone. This structure helps a complex effort remain organized and transparent.""",
    """Climate resilience requires communities to combine practical preparation with long-term investment. Cities can improve drainage, protect shade trees, modernize buildings, and give residents timely information during extreme weather. Each action is more effective when it includes the people who will use it, especially neighborhoods that face the greatest risk. Coordinated planning therefore strengthens both infrastructure and public confidence.""",
    """A strong learning routine balances focused practice, feedback, and rest. Students benefit from setting a small goal for each session, working without distractions, and checking their understanding with an example or short explanation. Feedback identifies gaps before they become habits, while breaks protect attention over time. The result is steady progress rather than a last-minute rush.""",
    """Good customer service depends on clarity, empathy, and follow-through. Staff should listen carefully, explain the available options in plain language, and state what will happen next. If a problem cannot be solved immediately, a realistic update is better than an uncertain promise. Consistent communication turns an ordinary interaction into a reliable experience.""",
]

SCENARIOS = [
    {"name": "my own writing", "criterion": 1, "texts": USER_WRITING},
    {"name": "label coverage", "criterion": 2, "texts": [
        USER_WRITING[3], USER_WRITING[7],
        USER_WRITING[0] + "\n\n" + AI_CONTROL[0],
        USER_WRITING[4] + "\n\n" + AI_CONTROL[1],
        AI_CONTROL[0], AI_CONTROL[1],
    ]},
    # These submissions create content IDs for the separate /appeal checks.
    {"name": "appeal setup", "criterion": 3,
     "texts": [AI_CONTROL[0], USER_WRITING[0] + "\n\n" + AI_CONTROL[0]]},
    {"name": "bad input and recovery", "criterion": 4, "bodies": [
        {"text": "", "creator_id": "eval_bad_empty"},
        {"creator_id": "eval_bad_missing"},
        {"text": "A request with no creator identifier.", "creator_id": ""},
        {"text": "A request with the creator identifier omitted."},
        {"text": "word " * 3000, "creator_id": "eval_bad_huge"},
        {"text": "A short valid recovery submission after rejected input.", "creator_id": "eval_bad_recovery"},
    ]},
    {"name": "score separation", "criterion": 5,
     "texts": USER_WRITING[:5] + AI_CONTROL},
]


def validate() -> list[str]:
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")
        texts, bodies = scenario.get("texts"), scenario.get("bodies")
        if texts and bodies:
            problems.append(f"scenario {i} has both texts and bodies")
        elif bodies and any(not isinstance(body, dict) for body in bodies):
            problems.append(f"scenario {i} has a body that is not a dict")
        elif not texts and not bodies:
            problems.append(f"scenario {i} has no texts and no bodies")
    return problems
