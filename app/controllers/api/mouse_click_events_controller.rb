class Api::MouseClickEventsController < ApplicationController
  include Epochable
  include Showable
  include Indexable
  include Createable

  private

  def parameters
    params.require(:mouse_click_event).permit(:session_id, :created_at)
  end
end
