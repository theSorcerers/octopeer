class Api::ChangeTabEventsController < ApplicationController
  include Epochable
  include Showable
  include Indexable
  include Createable

  private

  def parameters
    params.require(:change_tab_event).permit(:session_id, :url, :created_at)
  end
end
