class CreateChangeTabEvents < ActiveRecord::Migration[5.0]
  def change
    create_table :change_tab_events do |t|
      t.references :session, foreign_key: true
      t.string :url

      t.timestamps
    end
  end
end
