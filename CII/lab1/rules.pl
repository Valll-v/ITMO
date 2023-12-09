% One args rules
% heroes
% Types of play style
support(cristal_maiden).
support(bane).
support(pudge).
support(shaman).
support(demon).

core(queen_of_pain).
core(zeus).
core(anti_mage).
core(slark).
core(sven).


% Types of damage
magic_damage(pudge).
magic_damage(queen_of_pain).
magic_damage(zeus).

physical_damage(slark).
physical_damage(sven).
physical_damage(anti_mage).


% possibility to kill
easy_to_kill(cristal_maiden).
easy_to_kill(zeus).
easy_to_kill(shaman).
easy_to_kill(demon).
easy_to_kill(bane).


% agile heroes
agile(anti_mage).
agile(queen_of_pain).


% type of items (purpose)
mage_damage_item(dagon).
mage_damage_item(kaya).
mage_damage_item(ethereal).

phys_damage_item(silver_edge).
phys_damage_item(orchide).
phys_damage_item(eye_of_skadi).

shield_item(pipe).
shield_item(heart).
shield_item(guardian).


% type of items (possibility to bye)
core_game_role_item(dagon).
core_game_role_item(ethereal).
core_game_role_item(silver_edge).
core_game_role_item(eye_of_skadi).
core_game_role_item(heart).

support_item(pipe).
support_item(guardian).


% Two args rules
% items favorites
must_have_for_hero(slark, eye_of_skadi).
must_have_for_hero(slark, orchide).
must_have_for_hero(zeus, dagon).
must_have_for_hero(zeus, ethereal).
must_have_for_hero(queen_of_pain, dagon).
must_have_for_hero(queen_of_pain, ethereal).
must_have_for_hero(queen_of_pain, orchide).
must_have_for_hero(sven, silver_edge).


% synergy
good_with(ethereal, dagon).
good_with(silver_edge, orchide).
good_with(pipe, guardian).


% relations
% good item to bye for hero
good_for_hero(X, Y) :- must_have_for_hero(X, Y);
                       ((good_with(Y, Z), must_have_for_hero(X, Z));(good_with(Z, Y), must_have_for_hero(X, Z)));
                       (((magic_damage(X), mage_damage_item(Y));
                       (physical_damage(X), phys_damage_item(Y));
                       (easy_to_kill(X), shield_item(Y))), (
                                                           (support(X), not(core_game_role_item(Y)));
                                                           (core(X), not(support_item(Y)))
                                                           )
                       ).

% hero X bad vs hero Y
bad_versus(X, Y) :- (X == slark, Y = demon);
                    (not(easy_to_kill(X)), Y=slark);
                    (easy_to_kill(X), agile(Y)).

% support with core is always good team.
good_in_one_team(X, Y) :- (support(X), core(Y));
                          (core(Y), support(X)).

% supports and cores balance (able to realize with "good_in_one_team")
balanced_team(X, Y, Z) :- (support(X), (core(Y); core(Z)));
                          (support(Y), (core(X); core(Z)));
                          (support(Z), (core(Y); core(X))).

% magic and phys damage balance
good_team_fight_team(X, Y, Z) :- (physical_damage(X), (magic_damage(Y); magic_damage(Z)));
                                 (physical_damage(Y), (magic_damage(X); magic_damage(Z)));
                                 (physical_damage(Z), (magic_damage(Y); magic_damage(X))).

perfect_team(X, Y, Z) :- balanced_team(X, Y, Z), good_team_fight_team(X, Y, Z).
