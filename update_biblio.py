html = open('index.html', encoding='utf-8').read()

biblio_start = html.find("    <!-- PAGE 12: BIBLIOGRAPHY & QR -->")

new_biblio = """    <!-- PAGE 13: ANNOTATED BIBLIOGRAPHY (ARCHIVE) -->
    <div class="print-page">
      <header class="print-only page-header">
        <span class="meta-info">Group 2: Issy Beresford, Angelo Sanchez Dela Cruz, Clara Goudy, Cici Liu, Rania Xeptiana Ramadhani, & Amelia Zolidis de Navacelle</span>
        <span class="meta-info">Page 13</span>
      </header>

      <main>
        <section>
          <h2>X. Annotated Bibliography</h2>
          
          <h3>On ARCHIVE</h3>
          <ul class="inquiries-list">
            <li><u><strong>Stuart Hall</strong></u> — Constituting an Archive (2001)<br>
            As they aren’t neutral collections of the past, archives are shaped by decisions regarding what is kept, what is excluded, how things are organised. In this matter, they don’t just store history, they actively construct how we look at it and interpret it.</li>
            
            <li><u><strong>Saidiya Hartman</strong></u> — Venus in Two Acts (2008)<br>
            Archives never fully tell the lives they record as they reduce people to fragments, often administrative traces, and leave a lot unsaid. Hartman insists on working with these gaps, notably by acknowledging absence instead of trying to fill it completely.</li>
            
            <li><u><strong>Michelle Caswell</strong></u> — Urgent Archives (2021)<br>
            Caswell argues that archives can move beyond preservation to become tools for care, recognition, and social justice. She focuses on how communities can reclaim and reshape archives to repair histories that were neglected or misrepresented. Archives can be understood as active spaces of responsibility, not just storage.</li>

            <li><u><strong>Okwui Enwezor</strong></u> — Archive Fever (2008)<br>
            Contemporary artists treat archives as material to be reworked rather than preserved as stable truth. Through rearrangement, fragmentation, and juxtaposition, archives become unstable and open to new meanings. The focus shifts from what the archive contains to how it is used and activated.</li>
          </ul>
        </section>
      </main>
    </div> <!-- End Page 13 -->

    <div class="page-break"></div>

    <!-- PAGE 14: ANNOTATED BIBLIOGRAPHY (SOUND) & QR -->
    <div class="print-page">
      <header class="print-only page-header">
        <span class="meta-info">Group 2: Issy Beresford, Angelo Sanchez Dela Cruz, Clara Goudy, Cici Liu, Rania Xeptiana Ramadhani, & Amelia Zolidis de Navacelle</span>
        <span class="meta-info">Page 14</span>
      </header>

      <main>
        <section>
          <h3>On SOUND</h3>
          <ul class="inquiries-list">
            <li><u><strong>Salomé Voegelin</strong></u> — Listening to Noise and Silence (2010)<br>
            Listening isn’t passive. We don’t just receive sound: we produce meaning through it. As sound doesn’t carry a fixed message, it shifts depending on context, attention, and experience. This signifies that every listening situation is unstable, open, and slightly different for each person.</li>
            
            <li><u><strong>Brandon LaBelle</strong></u> — Acoustic Territories (2010)<br>
            Sound shapes how we experience space and how we relate to others within it. You don’t necessarily need direct interaction, listening in the same environment already creates a shared condition. It produces a kind of temporary, subtle and intangible community.</li>
            
            <li><u><strong>Nina Sun Eidsheim</strong></u> — The Race of Sound (2019)<br>
            A voice is never only a sound or words: it is embedded in identity, history, and social meaning. Moreover, what we hear is shaped by perception, expectation, and context. Listening can therefore never be seen as neutral, it is always an interpretative and subjective act.</li>
            
            <li><u><strong>Susan Philipsz</strong></u> — Lowlands (2010)<br>
            Her work uses recorded voice without a visible body, which creates a strong sense of absence. This would have had the effect of amplifying the sense of disembodiment of the voice(s) which feels present, but also incomplete: like a trace of someone no longer there. This produces a quiet, haunting relationship to space and memory.</li>
            
            <li><u><strong>Janet Cardiff</strong></u> & <u><strong>George Bures Miller</strong></u> — The Forty-Part Motet (2001)<br>
            They separate voices in space so you can walk between them. In their words, this enables the audience to “move throughout the space, allowing them to be intimately connected with the voices. It also reveals the piece as a changing construct”. It also reflects on “how sound may physically construct a space in a sculptural way and how a viewer may choose a path through this physical yet virtual space”.</li>
          </ul>
          
          <p>The event is constructed around bringing these ideas together. The archive is structured/structural and incomplete, while sound is experiential and relational. Thus, the installation becomes a space where listening acts as a counter/ reparative strategies of reanimation to recompose and create a lived archive, in a participatory and attentive reconstruction of memory.</p>
        </section>
        
        <div class="qr-container print-only" style="margin-top: 40pt;">
          <div class="qr-code-box">
            <img src="assets/qr_code.png" alt="Digital Leaflet QR Code">
            <p class="qr-caption">Scan for Digital Appx</p>
          </div>
          <div class="qr-code-box">
            <img src="assets/qr_code.png" alt="Audio Experience QR Code">
            <p class="qr-caption">Scan for Sonic Exp</p>
          </div>
        </div>
      </main>

      <footer>
        <p>Voices, Rights, and Future | Foundling Museum Activation | 2026</p>
      </footer>
    </div> <!-- End Page 14 -->
"""

html = html[:biblio_start] + new_biblio + "\n  </div>\n</body>\n</html>\n"

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Bibliography updated successfully!")
