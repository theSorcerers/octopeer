class CreateMouseClickEvents < ActiveRecord::Migration[5.0]
  def change
    create_table :mouse_click_events do |t|
      t.references :session, foreign_key: true

      t.timestamps
    end
  end
end
