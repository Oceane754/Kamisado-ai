import time
import pytest
import strategie

def test_choose_move_temps_execution():
    etat_du_jeu_fictif = {
  "board": [
    [
      ["orange", ["pink", "light"]],
      ["blue", ["orange", "light"]],
      ["purple", ["green", "light"]],
      ["pink", ["red", "light"]],
      ["yellow", ["purple", "light"]],
      ["red", ["blue", "light"]],
      ["green", ["brown", "light"]],
      ["brown", ["yellow", "light"]]
    ],
    [
      ["red", None],
      ["orange", None],
      ["pink", None],
      ["green", None],
      ["blue", None],
      ["yellow", None],
      ["brown", None],
      ["purple", None]
    ],
    [
      ["green", None],
      ["pink", None],
      ["orange", None],
      ["red", None],
      ["purple", None],
      ["brown", None],
      ["yellow", None],
      ["blue", None]
    ],
    [
      ["pink", None],
      ["purple", None],
      ["blue", None],
      ["orange", None],
      ["brown", None],
      ["green", None],
      ["red", None],
      ["yellow", None]
    ],
    [
      ["yellow", None],
      ["red", None],
      ["green", None],
      ["brown", None],
      ["orange", None],
      ["blue", None],
      ["purple", None],
      ["pink", None]
    ],
    [
      ["blue", None],
      ["yellow", None],
      ["brown", None],
      ["purple", None],
      ["red", None],
      ["orange", None],
      ["pink", None],
      ["green", None]
    ],
    [
      ["purple", None],
      ["brown", None],
      ["yellow", None],
      ["blue", None],
      ["green", None],
      ["pink", None],
      ["orange", None],
      ["red", None]
    ],
    [
      ["brown", ["yellow", "dark"]],
      ["green", ["green", "dark"]],
      ["red", ["orange", "dark"]],
      ["yellow", ["purple", "dark"]],
      ["pink", ["red", "dark"]],
      ["purple", ["brown", "dark"]],
      ["blue", ["blue", "dark"]],
      ["orange", ["pink", "dark"]]
    ]
  ],
  "color": None,
  "current": 0,
  "players": ["TLC", "TLC_RIVAL"]
}
    # Lancement du chrono
    start_time = time.time()
    
    move = strategie.choose_move(etat_du_jeu_fictif)
    
    end_time = time.time()
    temps_execution = end_time - start_time
    
    print(f"\n Le coup a été calculé en : {temps_execution:.3f} secondes.")

    # Vérification du respect de la condition avec assert
    assert temps_execution < 2.8, f"Échec : Notre IA est trop lente ! Temps : {temps_execution:.3f} secondes."
    assert move is not None, f"Échec : Notre IA n'a retourné aucun coup valide..."